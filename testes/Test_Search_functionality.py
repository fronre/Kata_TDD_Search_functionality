from src.Search_functionality import search_cities

def test_search_with_different_case_should_fail_initially():
    assert search_cities("Ba") == ["barcalona", "barsd", "bars"]

def test_search_text_inside_word_should_fail_initially():
    assert search_cities("can") == ["barcelona"]