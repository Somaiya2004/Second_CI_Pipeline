import importlib.util
import pathlib
codes_dir = pathlib.Path(__file__).parent.parent / "codes_4"
spec = importlib.util.spec_from_file_location("31_pangram", codes_dir / "31_pangram.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
is_pangram = mod.is_pangram

def test_pangram_true():
    assert is_pangram("The quick brown fox jumps over the lazy dog") == True
def test_pangram_false():
    assert is_pangram("Hello World") == False
