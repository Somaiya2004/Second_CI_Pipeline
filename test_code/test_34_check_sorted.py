import importlib.util
import pathlib

codes_dir = pathlib.Path(__file__).parent.parent / "codes"
spec = importlib.util.spec_from_file_location("34_check_sorted", codes_dir / "34_check_sorted.py")
sorted_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sorted_mod)
is_sorted = sorted_mod.is_sorted

def test_sorted_true():
    assert is_sorted([1, 2, 3, 4, 5]) == True
def test_sorted_false():
    assert is_sorted([1, 3, 2, 4]) == False
