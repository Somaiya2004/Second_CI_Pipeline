"""Program 33: Find the first non-repeating character."""
def first_non_repeating_char(s):
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char in s:
        if char_counts[char] == 1:
            return char
    return None
