import importlib
mf_mod = importlib.import_module("36_most_frequent")
most_frequent = mf_mod.most_frequent
def test_most_frequent():
    assert most_frequent([1, 2, 3, 2, 2, 4]) == 2
