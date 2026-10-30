"""Program 34: Check whether a list is sorted."""
def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr) - 1))
