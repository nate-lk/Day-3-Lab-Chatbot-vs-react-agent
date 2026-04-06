# Individual Report: Lab 3 - Chatbot vs ReAct Agent

- **Student Name**: Khương Hải Lâm
- **Student ID**: 2A202600088
- **Date**: 06/04/2026

---

## I. Technical Contribution (15 Points)

*Describe your specific contribution to the codebase (e.g., implemented a specific tool, fixed the parser, etc.).*

- **Modules Implementated**: src/tools/geo_tools. I implement this tool to find out the distance between the two places so users know the expected travel time
- **Code Highlights**: Code highlight is provided as follow
```
# geo_tools.py

from typing import TypedDict
import math
import os
import re


class Location(TypedDict):
    lat: float
    lon: float


def _load_cities() -> dict:
    """Load city coordinates from database.md"""
    db_path = os.path.join(os.path.dirname(__file__), "database.md")
    city_map = {}

    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database file not found: {db_path}")

    with open(db_path, 'r') as f:
        content = f.read()

    # Extract Cities section
    cities_section = re.search(r'## Cities\n(.*?)\n## ', content, re.DOTALL)
    if not cities_section:
        raise ValueError("Cities section not found in database.md")

    lines = cities_section.group(1).strip().split('\n')
    for line in lines:
        # Skip header and separator lines
        if line.startswith('|') and not line.startswith('| City') and '-' not in line:
            parts = [p.strip() for p in line.split('|')[1:-1]]
            if len(parts) == 3 and parts[1] and parts[2]:  # Ensure parts are not empty
                city, lat, lon = parts
                try:
                    city_map[city.lower()] = {"lat": float(lat), "lon": float(lon)}
                except ValueError:
                    # Skip lines that can't be parsed as floats
                    pass

    return city_map


def geocode(city: str) -> Location:
    city_map = _load_cities()
    key = city.lower()
    if key not in city_map:
        raise ValueError(f"Unknown city: '{city}'. Known cities: {list(city_map.keys())}")
    return city_map[key]


def haversine(loc1: Location, loc2: Location) -> float:
    R = 6371
    phi1    = math.radians(loc1["lat"])
    phi2    = math.radians(loc2["lat"])
    dphi    = math.radians(loc2["lat"] - loc1["lat"])
    dlambda = math.radians(loc2["lon"] - loc1["lon"])
    a = (
        math.sin(dphi / 2) ** 2
        + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    return round(R * c, 2)


def get_distance(city1: str, city2: str) -> str:
    loc1 = geocode(city1)
    loc2 = geocode(city2)
    km   = haversine(loc1, loc2)
    return f"{km} km"


# Tool definition — includes "fn" so the agent can call it directly
tool_schema = {
    "name":        "get_distance",
    "description": "Calculate the distance in km between two cities by name.",
    "fn":          get_distance,          # ← callable attached here
    "parameters": {
        "type": "object",
        "properties": {
            "city1": {"type": "string"},
            "city2": {"type": "string"},
        },
        "required": ["city1", "city2"],
    },
}


if __name__ == "__main__":
    print(get_distance("Hanoi", "Ho Chi Minh City"))
```

- **Documentation**: This prompt the model to get the coordination of the locations, and use trigonometry to figure out the distance between two places. But, the coordination must be defined in this mock database, we do not have access to real time data.

---

## II. Debugging Case Study (10 Points)

*Analyze a specific failure event you encountered during the lab using the logging system.*

- **Problem Description**: The thought process is not optimised for Vietnamese. Also, the bot cannot access the database if we do not have real data (mocked in this case)
- **Diagnosis**: The chat bot thought process is not optimised for Vietnamese, thus, it uses unicode for non-standard English character. This can lead to excess or unnecessary token consumption, increase the price and lower ROI if applied in large scale
- **Solution**: Another models that is native or optimised for Vietnamese (like the models provided by Viettel or FPT, will mitigate this situation)

---

## III. Personal Insights: Chatbot vs ReAct (10 Points)



*Reflect on the reasoning capability difference.*

1.  **Reasoning**: The Thought box helps the agent to sequentially access the tools. For example, in this project we provide 4 tools, and for each tool, the thought process helps the agent to access one tool at a time.
2.  **Reliability**: If there is a loop in place that exceed the maximum sequence of thought, or the final answer is not met, the chatbot does not provide the final answer to the customer. In this case, a pure LLM would perform better.
3.  **Observation**: The chatbot analyses observations, and because it requires enough information from the user, this will prevent or mitigate the hallucinated answer.

---

## IV. Future Improvements (5 Points)

*How would you scale this for a production-level AI agent system?*

- **Scalability**: The thought process in this educational session is sequential, thus it might increase the wait time of the customer, leading to poor UX. 
- **Safety**: There must be a measure of security in place. This is purely an educational mocking tool, so there is no Prompt injection prevention
- **Performance**: Vector DB is necessary to index the data, which would be a vast improvement from this educational session. Also, prompt engineering in a better way can reduce the usage of token.

---

> [!NOTE]
> Submit this report by renaming it to `REPORT_[YOUR_NAME].md` and placing it in this folder.
