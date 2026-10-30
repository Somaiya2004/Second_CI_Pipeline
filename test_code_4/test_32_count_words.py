import importlib.util
import pathlib
codes_dir = pathlib.Path(__file__).parent.parent / "codes_4"
spec = importlib.util.spec_from_file_location("32_count_words", codes_dir / "32_count_words.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
count_words = mod.count_words

def test_count_words_basic():
    assert count_words("Hello world from Python") == 4
def test_count_words_empty():
    assert count_words("") == 0
