"""Program 38: Missing number using XOR."""
def find_missing_number(arr):
    n = len(arr)
    xor_all = sum(range(n + 1))
    return xor_all - sum(arr)
