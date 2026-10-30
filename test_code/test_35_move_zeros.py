import importlib.util
import pathlib

codes_dir = pathlib.Path(__file__).parent.parent / "codes"
spec = importlib.util.spec_from_file_location("35_move_zeros", codes_dir / "35_move_zeros.py")
mz_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mz_mod)
move_zeros_to_end = mz_mod.move_zeros_to_end

def test_move_zeros():
    assert move_zeros_to_end([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
