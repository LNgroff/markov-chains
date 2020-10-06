"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    contents = open(file_path).read()

    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # Tokenize text
    tokens = text_string.split()  # Returns [word1, word2, word3]

    # Assign macro for tuple-formatted key
    bigram = '(tokens[i], tokens[i + 1])'

    # Loop through tokenized text and track pairs of words
    for i in range(len(tokens) - 2):
        chains[eval(bigram)] = []

    # Loop through the keys in chain and if match, add following word to list as key-value
    for i in range(len(tokens) - 1):
        if eval(bigram) in chains.keys():
            chains[eval(bigram)].append(tokens[i + 2])

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # Return random key
    random_key = choice(list(chains))

    # Destructure and append the beginning words to word list
    words1, words2 = random_key
    words.append(words1)
    words.append(words2)

    # Initialize bigram lookup with random key
    bigram_lookup = chains.get(random_key) # Returns list of probable next words or None

    next_bigram = '(words[-2], words[-1])'

    # Continue to loop until .get() returns None
    while True:
        # Add the next bigram to eval
        if bigram_lookup:
            words.append(choice(bigram_lookup))

            # Reassigns bigram for the next loop
            bigram_lookup = chains.get(eval(next_bigram))
        else:
            break

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
