import importlib.util
import pathlib

codes_dir = pathlib.Path(__file__).parent.parent / "codes"
spec = importlib.util.spec_from_file_location("40_gcd", codes_dir / "40_gcd.py")
gcd_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gcd_mod)
find_gcd = gcd_mod.find_gcd

def test_gcd():
    assert find_gcd(48, 18) == 6
