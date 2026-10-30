import importlib.util
import pathlib
codes_dir = pathlib.Path(__file__).parent.parent / "codes_4"
spec = importlib.util.spec_from_file_location("36_most_frequent", codes_dir / "36_most_frequent.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
most_frequent = mod.most_frequent

def test_most_frequent():
    assert most_frequent([1, 2, 3, 2, 2, 4]) == 2
