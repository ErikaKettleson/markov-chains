from random import choice

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_string = open(file_path).read()
    return text_string

    "This should be a variable that contains your file text as one long string"


def make_chains(text_string):
    """Takes input text as string; returns _dictionary_ of markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> make_chains("hi there mary hi there juanita")
        {('hi', 'there'): ['mary', 'juanita'], ('there', 'mary'): ['hi'], ('mary', 'hi': ['there']}
    """

    chains = {}
    current_key = ()
    words = text_string.split()
    words.append(None)

    for index in range(len(words) - 2):
        bi_gram = words[index], words[index + 1]
        bi_gram_value = chains.get(bi_gram, [])
        bi_gram_value.append(words[index + 2])
        chains[bi_gram] = bi_gram_value
    return chains



def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""

    # result = ""
    # bi_gram1 = choice(chains.keys())
    # for bi_gram in chains:
    #     ran_value = choice(chains.values())
    #     new_bi_gram = bi_gram[1] + ran_value[0]
    #     print new_bi_gram


    # for bi_gram in chains:
    #     current_bi_gram = choice(chains.keys())
    #     chains[current_bi_gram] current_bi_gram
    #     print current_bi_gram

    # random_text = bi_gram1[0] + " " + bi_gram1[1] + " " + ran_value[0]
    # return random_text


    # Get random bi_gram to start
    starting_bi_gram = choice(chains.keys())
    # store first two words in list
    markov_words = list(starting_bi_gram)


    current_bi_gram = starting_bi_gram
    while True:
        # Get the next word by choosing word from value of current bigram
        next_word = choice(chains[current_bi_gram])
        # if next_word is None:
        if not next_word: # We reached the end of the text
            break
        # Storing next word in list
        markov_words.append(next_word)
        # reassigning current_bi_gram to the second word & the next_word
        current_bi_gram = current_bi_gram[1:] + (next_word,)

    # joining list into one string and returning it
    return " ".join(markov_words)




input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
