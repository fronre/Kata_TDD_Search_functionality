from src.Search_functionality import search_cities

def test_search_with_different_case_should_pass_now():
    assert search_cities("Ba") == ["Bangkok", "Dubai"]

def test_search_text_inside_word_should_pass_now():
    assert search_cities("gko") == ["Bangkok"]

def test_search_no_match_returns_empty():
    assert search_cities("zzz") == []

def test_search_match_at_end_of_word():
    assert search_cities("ris") == ["Paris"]

def test_search_with_asterisk_returns_all_cities():

    assert search_cities("*") == [
        "Paris", "Budapest", "Skopje", "Rotterdam", "Valencia", "Vancouver",
        "Amsterdam", "Vienna", "Sydney", "New York City", "London",
        "Bangkok", "Hong Kong", "Dubai", "Rome", "Istanbul"
    ]
