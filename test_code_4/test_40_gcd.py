import importlib.util
import pathlib
codes_dir = pathlib.Path(__file__).parent.parent / "codes_4"
spec = importlib.util.spec_from_file_location("40_gcd", codes_dir / "40_gcd.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
find_gcd = mod.find_gcd

def test_gcd():
    assert find_gcd(48, 18) == 6
