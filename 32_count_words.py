"""Program 32: Count the number of words in a sentence."""
def count_words(sentence):
    if not sentence or not sentence.strip():
        return 0
    return len(sentence.strip().split())
