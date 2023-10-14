"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 20
Actual: 35
"""


def main():
    text = (input("Text: ")).split()
    word_to_count = {}
    largest_word = ""
    largest_word = create_dictionary(largest_word, text, word_to_count)
    print_dictionary_items(largest_word, word_to_count)


def create_dictionary(largest_word, text, word_to_count):
    """Assigns count of words to word in a dictionary"""
    for word in text:
        word_to_count[word] = text.count(word)
        largest_word = determine_largest_word(largest_word, word)
    return largest_word


def determine_largest_word(largest_word, word):
    """Determines largest word in string"""
    if len(word) > len(largest_word):
        largest_word = word
    return largest_word


def print_dictionary_items(largest_word, word_to_count):
    """Prints keys with values from dictionary"""
    for word in word_to_count:
        print(f"{word:{len(largest_word)}} : {word_to_count[word]}")


main()
