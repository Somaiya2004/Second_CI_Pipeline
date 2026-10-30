import importlib
words_mod = importlib.import_module("32_count_words")
count_words = words_mod.count_words
def test_count_words_basic():
    assert count_words("Hello world from Python") == 4
def test_count_words_empty():
    assert count_words("") == 0
