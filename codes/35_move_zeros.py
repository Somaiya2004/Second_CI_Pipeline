"""Program 35: Move all zeros to the end."""
def move_zeros_to_end(arr):
    non_zeros = [x for x in arr if x != 0]
    zeros = [0] * (len(arr) - len(non_zeros))
    return non_zeros + zeros
