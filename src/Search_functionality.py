def search_cities(search_text: str) -> list:
    cities = ["barcelona", "barsd", "bars", "paris"]

    if len(search_text) < 2:
        return []

    search_text = search_text.lower()

    result = []
    for city in cities:
        if search_text in city.lower():
            result.append(city)
    return result
