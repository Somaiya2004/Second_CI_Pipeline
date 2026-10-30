import importlib.util
import pathlib

codes_dir = pathlib.Path(__file__).parent.parent / "codes"
spec = importlib.util.spec_from_file_location("32_count_words", codes_dir / "32_count_words.py")
words_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(words_mod)
count_words = words_mod.count_words

def test_count_words_basic():
    assert count_words("Hello world from Python") == 4
def test_count_words_empty():
    assert count_words("") == 0
