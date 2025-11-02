def search_cities(search_text: str) -> list:
    cities = [
        "Paris", "Budapest", "Skopje", "Rotterdam", "Valencia", "Vancouver",
        "Amsterdam", "Vienna", "Sydney", "New York City", "London",
        "Bangkok", "Hong Kong", "Dubai", "Rome", "Istanbul"
    ]

    search_text = search_text.strip()

    if len(search_text) < 2:
        return []

    if search_text == "*":
        return cities

    result = []
    for city in cities:
        if search_text.lower() in city.lower():
            result.append(city)
    return result
