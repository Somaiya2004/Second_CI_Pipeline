import importlib
pangram_mod = importlib.import_module("31_pangram")
is_pangram = pangram_mod.is_pangram
def test_pangram_true():
    assert is_pangram("The quick brown fox jumps over the lazy dog") == True
def test_pangram_false():
    assert is_pangram("Hello World") == False
