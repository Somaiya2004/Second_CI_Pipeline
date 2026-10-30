import importlib
mn_mod = importlib.import_module("38_missing_number_xor")
find_missing_number = mn_mod.find_missing_number
def test_missing():
    assert find_missing_number([3, 0, 1]) == 2
