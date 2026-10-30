import importlib.util
import pathlib
codes_dir = pathlib.Path(__file__).parent.parent / "codes_4"
spec = importlib.util.spec_from_file_location("37_rotate_string", codes_dir / "37_rotate_string.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
rotate_string = mod.rotate_string

def test_rotate():
    assert rotate_string("abcdef", 2) == "efabcd"
