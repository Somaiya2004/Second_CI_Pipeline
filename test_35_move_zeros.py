import importlib
mz_mod = importlib.import_module("35_move_zeros")
move_zeros_to_end = mz_mod.move_zeros_to_end
def test_move_zeros():
    assert move_zeros_to_end([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
