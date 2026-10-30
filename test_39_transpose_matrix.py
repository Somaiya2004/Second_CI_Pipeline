import importlib
tm_mod = importlib.import_module("39_transpose_matrix")
transpose_matrix = tm_mod.transpose_matrix
def test_transpose():
    assert transpose_matrix([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]
