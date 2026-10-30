"""Program 36: Most frequent element."""
from collections import Counter
def most_frequent(arr):
    if not arr: return None
    return Counter(arr).most_common(1)[0][0]
