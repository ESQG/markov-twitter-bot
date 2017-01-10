from random import choice


def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    with open(file_path, "r") as word_file:
        text = word_file.read()

    return text


def make_chains(text_string):
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

    for index, word in enumerate(words[:-2]):
        word_tuple = (words[index], words[index + 1])

        if word_tuple not in chains:
            chains[word_tuple] = [words[index + 2]]
        else:
            chains[word_tuple].append(words[index + 2])
    print chains.keys()[0]
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

    word_pair = choice(start_tuples)
    text = [word_pair[0], word_pair[1]]

    while word_pair in chains:

        next_word = choice(chains[word_pair])

        text.append(next_word)

        word_pair = (word_pair[1], next_word)

        if next_word[-1] == '.' and len(text) > 200:
            break

        if word_pair not in chains and len(text) < 20:
            word_pair = choice(start_tuples)
            text.extend(word_pair)

    return " ".join(text)


input_path = "twain.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
