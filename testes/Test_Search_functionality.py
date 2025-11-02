from src.Search_functionality import search_cities

def test_search_empty():
    assert search_cities("") == []
