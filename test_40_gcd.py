import importlib
gcd_mod = importlib.import_module("40_gcd")
find_gcd = gcd_mod.find_gcd
def test_gcd():
    assert find_gcd(48, 18) == 6
