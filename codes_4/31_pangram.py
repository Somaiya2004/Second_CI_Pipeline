"""Program 31: Check if a string is a pangram."""
import string
def is_pangram(text):
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(set(text.lower()))
