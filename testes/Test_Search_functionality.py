from src.Search_functionality import search_cities

def test_short_text_returns_empty():
    assert search_cities("b") == []
