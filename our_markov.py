from random import choice
import os
import twitter
import sys


def open_and_read_files(list_of_files):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text = ""

    for file_path in list_of_files:
        with open(file_path, "r") as word_file:
            text += word_file.read()+"\n"

    return text


def make_chains(text_string, chain_length): # Far from optimized.
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

    if chain_length < 1:
        print "Chain length must be at least 1."
        chain_length = int(raw_input("Please enter an appropriate chain length: "))

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

        if next_word[-1] in ".!?" and len(text) > 25:
            break

        if word_tuple not in chains and len(text) < 3:
            word_tuple = choice(start_tuples)
            text.extend(word_tuple)

    return " ".join(text)

def tweet(chains):
    # Use Python os.environ to get at environmental variables.
    # Note: you must run `source secrets.sh` before running this file
    # to make sure these environmental variables are set.
    tweet_contents = make_text(chains)
    while len(tweet_contents) > 140:
        tweet_contents = make_text(chains)
    # print tweet_contents

    api = twitter.Api(
        consumer_key=os.environ['TWITTER_CONSUMER_KEY'],
        consumer_secret=os.environ['TWITTER_CONSUMER_SECRET'],
        access_token_key=os.environ['TWITTER_ACCESS_TOKEN_KEY'],
        access_token_secret=os.environ['TWITTER_ACCESS_TOKEN_SECRET'],
        )

    status = api.PostUpdate(tweet_contents)
    print status.text


chain_length = int(sys.argv[-1])

# Open the file and turn it into one long string.
input_text = open_and_read_files(sys.argv[1:-1]) 

# Get a Markov chain.
random_content = make_chains(input_text, chain_length)

# Produce random text.
# random_text = make_text(chains)

# Your task is to write a new function tweet, that will take chains as input.
tweet(random_content)
