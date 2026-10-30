import importlib
sorted_mod = importlib.import_module("34_check_sorted")
is_sorted = sorted_mod.is_sorted
def test_sorted_true():
    assert is_sorted([1, 2, 3, 4, 5]) == True
def test_sorted_false():
    assert is_sorted([1, 3, 2, 4]) == False
