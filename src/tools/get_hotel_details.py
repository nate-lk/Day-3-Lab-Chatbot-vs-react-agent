from typing import Dict, List


# Mock dataset used for lab exercises.
HOTEL_DETAILS: Dict[str, Dict[str, object]] = {
    "HCM001": {
        "name": "Saigon Grand Hotel",
        "city": "Ho Chi Minh City",
        "star_rating": 5,
        "address": "123 Nguyen Hue Boulevard, District 1, HCMC",
        "price_per_night": 120,
        "amenities": {
            "pool": True,
            "gym": True,
            "spa": True,
            "restaurant": True,
            "bar": True,
            "free_wifi": True,
            "parking": True,
            "airport_shuttle": True,
            "room_service": True,
            "laundry": True,
            "business_center": True,
            "pet_friendly": False,
        },
        "room_types": ["Standard", "Deluxe", "Suite", "Presidential Suite"],
        "images": [
            "https://mock-cdn.example.com/HCM001/lobby.jpg",
            "https://mock-cdn.example.com/HCM001/pool.jpg",
            "https://mock-cdn.example.com/HCM001/deluxe-room.jpg",
        ],
        "policies": {
            "check_in": "14:00",
            "check_out": "12:00",
            "cancellation": "Free cancellation up to 24 hours before check-in.",
            "children": "Children under 6 stay free.",
            "smoking": "Non-smoking property. Designated outdoor areas available.",
            "payment": "Accepts Visa, MasterCard, JCB, and cash (VND, USD).",
        },
        "description": (
            "A landmark 5-star hotel in the heart of District 1. "
            "Walking distance to Ben Thanh Market and Reunification Palace. "
            "Rooftop infinity pool with panoramic city views."
        ),
    },
    "HAN002": {
        "name": "Hanoi Heritage Boutique",
        "city": "Hanoi",
        "star_rating": 4,
        "address": "45 Hang Bac Street, Hoan Kiem District, Hanoi",
        "price_per_night": 75,
        "amenities": {
            "pool": False,
            "gym": True,
            "spa": False,
            "restaurant": True,
            "bar": True,
            "free_wifi": True,
            "parking": False,
            "airport_shuttle": True,
            "room_service": True,
            "laundry": True,
            "business_center": False,
            "pet_friendly": False,
        },
        "room_types": ["Standard", "Superior", "Deluxe", "Junior Suite"],
        "images": [
            "https://mock-cdn.example.com/HAN002/facade.jpg",
            "https://mock-cdn.example.com/HAN002/superior-room.jpg",
            "https://mock-cdn.example.com/HAN002/restaurant.jpg",
        ],
        "policies": {
            "check_in": "15:00",
            "check_out": "11:00",
            "cancellation": "Free cancellation up to 48 hours before check-in.",
            "children": "Children under 12 stay free when sharing existing bedding.",
            "smoking": "Smoking permitted in designated balcony rooms only.",
            "payment": "Accepts Visa, MasterCard, and cash (VND).",
        },
        "description": (
            "A charming boutique hotel nestled in Hanoi's historic Old Quarter. "
            "French colonial architecture blended with traditional Vietnamese decor. "
            "Steps from Hoan Kiem Lake and night market streets."
        ),
    },
    "DAD003": {
        "name": "Da Nang Ocean Resort & Spa",
        "city": "Da Nang",
        "star_rating": 5,
        "address": "88 Vo Nguyen Giap Street, My Khe Beach, Da Nang",
        "price_per_night": 200,
        "amenities": {
            "pool": True,
            "gym": True,
            "spa": True,
            "restaurant": True,
            "bar": True,
            "free_wifi": True,
            "parking": True,
            "airport_shuttle": True,
            "room_service": True,
            "laundry": True,
            "business_center": True,
            "pet_friendly": False,
        },
        "room_types": ["Deluxe Sea View", "Premier Ocean", "Pool Villa", "Beachfront Suite"],
        "images": [
            "https://mock-cdn.example.com/DAD003/beachfront.jpg",
            "https://mock-cdn.example.com/DAD003/infinity-pool.jpg",
            "https://mock-cdn.example.com/DAD003/spa.jpg",
            "https://mock-cdn.example.com/DAD003/pool-villa.jpg",
        ],
        "policies": {
            "check_in": "14:00",
            "check_out": "12:00",
            "cancellation": "Free cancellation up to 72 hours before check-in. 1-night fee applies after.",
            "children": "Children under 12 stay free. Kids club available 08:00-18:00.",
            "smoking": "Non-smoking property.",
            "payment": "Accepts all major cards and cash (VND, USD, EUR).",
        },
        "description": (
            "A world-class beachfront resort directly on My Khe Beach. "
            "Award-winning spa, multiple dining outlets, and a private stretch of white sand. "
            "Ideal for families, couples, and wellness retreats."
        ),
    },
}


# Human-readable labels for amenity keys
AMENITY_LABELS: Dict[str, str] = {
    "pool": "Swimming Pool",
    "gym": "Fitness Center / Gym",
    "spa": "Spa & Wellness",
    "restaurant": "On-site Restaurant",
    "bar": "Bar / Lounge",
    "free_wifi": "Free Wi-Fi",
    "parking": "Free Parking",
    "airport_shuttle": "Airport Shuttle",
    "room_service": "24h Room Service",
    "laundry": "Laundry Service",
    "business_center": "Business Center",
    "pet_friendly": "Pet Friendly",
}


def _format_amenities(amenities: Dict[str, bool]) -> str:
    """Return two comma-separated lists: available and unavailable amenities."""
    available = [AMENITY_LABELS[k] for k, v in amenities.items() if v]
    unavailable = [AMENITY_LABELS[k] for k, v in amenities.items() if not v]
    result = f"Available: {', '.join(available)}" if available else "No listed amenities."
    if unavailable:
        result += f" | Not available: {', '.join(unavailable)}"
    return result


def _format_policies(policies: Dict[str, str]) -> str:
    """Return a bullet-style string of hotel policies."""
    lines = [
        f"  - Check-in: {policies.get('check_in', 'N/A')}",
        f"  - Check-out: {policies.get('check_out', 'N/A')}",
        f"  - Cancellation: {policies.get('cancellation', 'N/A')}",
        f"  - Children: {policies.get('children', 'N/A')}",
        f"  - Smoking: {policies.get('smoking', 'N/A')}",
        f"  - Payment: {policies.get('payment', 'N/A')}",
    ]
    return "\n".join(lines)


def get_hotel_details(hotel_id: str) -> str:
    """
    Return detailed information about a specific hotel, including amenities,
    available room types, image URLs, and key policies.

    Args:
        hotel_id: Hotel identifier (for example: HCM001, HAN002, DAD003).

    Returns:
        A formatted text summary covering the hotel's facilities, policies,
        and media links -- useful for answering guest questions such as
        "Does this hotel have a pool?" or "What is the cancellation policy?".
    """
    if not hotel_id:
        return "Invalid hotel_id. Please provide a non-empty hotel id."

    normalized_id = hotel_id.strip().upper()
    hotel = HOTEL_DETAILS.get(normalized_id)

    if not hotel:
        return (
            f"No detail data found for hotel_id={normalized_id}. "
            f"Available IDs: {', '.join(HOTEL_DETAILS.keys())}."
        )

    name: str = str(hotel["name"])
    city: str = str(hotel["city"])
    stars: int = int(hotel["star_rating"])          # type: ignore[arg-type]
    address: str = str(hotel["address"])
    price: int = int(hotel["price_per_night"])       # type: ignore[arg-type]
    description: str = str(hotel["description"])
    room_types: List[str] = list(hotel["room_types"])  # type: ignore[arg-type]
    images: List[str] = list(hotel["images"])           # type: ignore[arg-type]
    amenities: Dict[str, bool] = dict(hotel["amenities"])  # type: ignore[arg-type]
    policies: Dict[str, str] = dict(hotel["policies"])      # type: ignore[arg-type]

    amenity_summary = _format_amenities(amenities)
    policy_summary = _format_policies(policies)
    room_list = ", ".join(room_types)
    image_list = " | ".join(images)
    star_display = "★" * stars

    return (
        f"[{normalized_id}] {name} {star_display}\n"
        f"Location: {address}, {city}\n"
        f"Price: from ${price}/night\n\n"
        f"About: {description}\n\n"
        f"Amenities -- {amenity_summary}\n\n"
        f"Room Types: {room_list}\n\n"
        f"Policies:\n{policy_summary}\n\n"
        f"Images: {image_list}"
    )