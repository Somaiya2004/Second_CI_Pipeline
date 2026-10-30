import importlib
rs_mod = importlib.import_module("37_rotate_string")
rotate_string = rs_mod.rotate_string
def test_rotate():
    assert rotate_string("abcdef", 2) == "efabcd"
