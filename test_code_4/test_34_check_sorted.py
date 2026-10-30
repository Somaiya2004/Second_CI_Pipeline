import importlib.util
import pathlib
codes_dir = pathlib.Path(__file__).parent.parent / "codes_4"
spec = importlib.util.spec_from_file_location("34_check_sorted", codes_dir / "34_check_sorted.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
is_sorted = mod.is_sorted

def test_sorted_true():
    assert is_sorted([1, 2, 3, 4, 5]) == True
def test_sorted_false():
    assert is_sorted([1, 3, 2, 4]) == False
