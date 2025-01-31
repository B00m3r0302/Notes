import gensim.downloader as api
import os
import re
import unicodedata
import string

# Set the model for the llm
model = api.load("glove-twitter-25")

# Open the text file as an object
doc = open('chal.txt', encoding = 'utf-8')

# filter out non-ASCII characters with regular expressions using re
def remove_non_ascii(text):
    # First you have to normalize full-width characters to their ASCII equivelants to preserve meaning, give imporved readability and get better data processing
    text = unicodedata.normalize('NFKC', text) # Converts full-width characters and converts special unicode forms
    #Define allowed characters: ASCII letters, digits, punctuation and whitespace
    allowed_characters = string.ascii_letters + string.digits + string.punctuation + string.whitespace

    # Remove any remaining characters that are not in the allowed set
    return ''.join(c for c in text if c in allowed_characters)

# Regex pattern to match analogies in the format:
# "Like X is to Y, A is to?"
pattern = r"""
        \bLike\s+               # Match "Like " at the beginning, ensuring it's a full word (\b) and ensures spaces after it \s+
        ([\w\s]+?)\s+           # Capture X: one or more word characters (\w) or spaces lazily (+?)
        is\s+to\s+              # Match " is to " exactly
        ([\w\s]+?),\s+          # Capture Y: One or more word characters or spaces, followed by a comma and space
        ([\w\s]+?)\s+           # Capture A: One or more word characters or spaces lazily
        is\s+to                 # Match " is to " exactly
        \?                      # Match the ? at the end of each analogy
"""


# Open the input file chal.txt, process the text and save the cleaned output
with open("chal.txt", "r", encoding = "utf-8") as infile, open("chall.txt", "w", encoding = "ascii") as outfile:
    content = infile.read() # Read the entire file into a string

    # Uses re.findall to extract all matching analogies from the file contents
    matches = re.findall(pattern, content, re.VERBOSE)

    # Open the output file "chall.txt" for writing extracted analogies
    with open("chall.txt", "w", encoding="utf-8") as outfile:
        for match in matches:
            # Extract and print the words being compared
            X, Y, A = match
            
            # Try to find the word vectors for X, Y, A
            try:
                # Get the word vectors for X, Y, A
                vec_X = model[X.lower()]
                vec_Y = model[Y.lower()]
                vec_A = model[A.lower()]

                # Perform the analogy calculation: B = Y - X + A
                analogy_vector = vec_Y - vec_X + vec_A

                # Find the most similar word to the resulting vector (top 1 most similar word)
                result = model.similar_by_bector(analogy_vector, topn=1)

                # the word that is most similar to the resulting vector
                B = result[0][0]

                # Print the result (X is to Y as A is to B)
                print(f"Analogy: {X} is to {Y} as {A} is to {B}")

                # Write the result to the output file
                outfile.write(f"Analogy: {X} is to {Y} as {A} is to {B}")

            except KeyError as e:
                # Handle the case where one of the words is not in the model
                print(f"Word not found in model: {e}")
                continue
