"""Program 37: Rotate a string by K."""
def rotate_string(s, k):
    if not s: return s
    k = k % len(s)
    if k == 0: return s
    return s[-k:] + s[:-k]
