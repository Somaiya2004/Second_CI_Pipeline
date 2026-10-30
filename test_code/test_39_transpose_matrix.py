import importlib.util
import pathlib

codes_dir = pathlib.Path(__file__).parent.parent / "codes"
spec = importlib.util.spec_from_file_location("39_transpose_matrix", codes_dir / "39_transpose_matrix.py")
tm_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tm_mod)
transpose_matrix = tm_mod.transpose_matrix

def test_transpose():
    assert transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
