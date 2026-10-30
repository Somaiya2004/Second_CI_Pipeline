import importlib.util
import pathlib
codes_dir = pathlib.Path(__file__).parent.parent / "codes_4"
spec = importlib.util.spec_from_file_location("38_missing_number_xor", codes_dir / "38_missing_number_xor.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
find_missing_number = mod.find_missing_number

def test_missing():
    assert find_missing_number([3, 0, 1]) == 2
