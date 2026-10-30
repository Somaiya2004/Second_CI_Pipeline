import importlib.util
import pathlib
codes_dir = pathlib.Path(__file__).parent.parent / "codes_4"
spec = importlib.util.spec_from_file_location("33_first_non_repeating", codes_dir / "33_first_non_repeating.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
first_non_repeating_char = mod.first_non_repeating_char

def test_first_non_repeating_basic():
    assert first_non_repeating_char("swiss") == "w"
def test_first_non_repeating_none():
    assert first_non_repeating_char("aabbcc") is None
