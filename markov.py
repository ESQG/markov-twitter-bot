from random import choice

import sys


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path, "r") as word_file:
        text = word_file.read()

    return text


def make_chains(text_string, chain_length):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that fobreakllow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    words = text_string.split()

    for index, word in enumerate(words[:-chain_length]):
        word_tuple = tuple(words[index: index + chain_length])

        if word_tuple not in chains:
            chains[word_tuple] = [words[index + chain_length]]
        else:
            chains[word_tuple].append(words[index + chain_length])

    return chains


def make_start_tuples(chains):
    start_tuples = []
    for word_tuple in chains:
        if word_tuple[0][0].isupper():
            start_tuples.append(word_tuple)

    return start_tuples


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    start_tuples = make_start_tuples(chains)

    word_tuple = choice(start_tuples)
    text = list(word_tuple)

    while word_tuple in chains:

        next_word = choice(chains[word_tuple])

        text.append(next_word)

        word_tuple = word_tuple[1:] + (next_word,)

        if next_word[-1] == '.' and len(text) > 200:
            break

        if word_tuple not in chains and len(text) < 20:
            word_tuple = choice(start_tuples)
            text.extend(word_tuple)

    return " ".join(text)


input_path = sys.argv[1]

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text, 3)

# Produce random text
random_text = make_text(chains)

print random_text
