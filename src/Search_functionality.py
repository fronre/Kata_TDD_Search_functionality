def search_cities(search_text: str) -> list:
    cities = ["barchalna", "barsd", "bars"]

    if len(search_text) < 2:
        return []

    result = []
    for city in cities:
        if city.lower().startswith(search_text.lower()):
            result.append(city)
    return result
