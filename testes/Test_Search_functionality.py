import pytest
from src.Search_functionality import search_cities

@pytest.mark.parametrize("search_text, expected", [
    ("Ba", ["Bangkok", "Dubai"]),
    ("gko", ["Bangkok"]),
    ("zzz", []),
    ("ris", ["Paris"]),
    ("*", [
        "Paris", "Budapest", "Skopje", "Rotterdam", "Valencia", "Vancouver",
        "Amsterdam", "Vienna", "Sydney", "New York City", "London",
        "Bangkok", "Hong Kong", "Dubai", "Rome", "Istanbul"
    ])
])
def test_search_cities(search_text, expected):
    assert search_cities(search_text) == expected
