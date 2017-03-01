from random import choice

def open_and_read_file(file_path):
    """Takes file path as string; returns text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    text_string = open(file_path).read()
    return text_string.split()

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

    for index in range(len(text_string) - 2):
        bi_gram = text_string[index], text_string[index + 1]
        bi_gram_value = chains.get(bi_gram, [])
        bi_gram_value.append(text_string[index + 2])
        chains[bi_gram] = bi_gram_value
    return chains



def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""
    result = ""
    bi_gram1 = choice(chains.keys())
    ran_value = choice(chains.values())
    random_text = bi_gram1[0] + " " + bi_gram1[1] + " " + ran_value[0]
    print random_text

    # for bi_gram in chains:
    #     random_value = choice(chains[bi_gram])
    #     random_text = [(bi_gram, random_value) for bi_gram in chains]
    #     # random_text = random_text + random_value
    #     # print type(random_text), type(random_value)



input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print random_text
