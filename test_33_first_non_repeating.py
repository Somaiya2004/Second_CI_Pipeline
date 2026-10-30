import importlib
fnr_mod = importlib.import_module("33_first_non_repeating")
first_non_repeating_char = fnr_mod.first_non_repeating_char
def test_first_non_repeating_basic():
    assert first_non_repeating_char("swiss") == "w"
def test_first_non_repeating_none():
    assert first_non_repeating_char("aabbcc") is None
