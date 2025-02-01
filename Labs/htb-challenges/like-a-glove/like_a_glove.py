import gensim.downloader as api
import re
import string

# Load the GloVe model for word vectors
model = api.load("glove-twitter-25")

# File path to the challenge file
file_path = "chal.txt"

# Variable to accumulate the flag (result) string
flag = ""

# Mapping full-width characters to ASCII characters
full_width_map = {
    "０": "0", "１": "1", "２": "2", "３": "3", "４": "4", "５": "5",
    "６": "6", "７": "7", "８": "8", "９": "9",
    # You can add any other full-width characters here if needed
}

# Helper function to remove non-ASCII characters and map full-width characters to ASCII
def keep_ascii_and_digits(text):
    # Normalize full-width characters to ASCII equivalents (e.g., ０ → 0)
    normalized_text = "".join(full_width_map.get(c, c) for c in text)
    # Return only ASCII letters, digits, punctuation, and whitespace
    return "".join(c for c in normalized_text if c in string.ascii_letters + string.digits + string.punctuation + string.whitespace)

# Regex pattern to match analogies in the format "Like X is to Y, A is to?"
pattern = re.compile(r"^Like ([^\s]+) is to ([^\s]+), ([^\s]+) is to\?$")

# Open and read the input file line by line
with open(file_path, "r") as file:
    for line in file:
        try:
            # Use regex to extract the words from the analogy format
            match = pattern.match(line.strip())
            if not match:
                print(f"Skipping line due to incorrect format: {line}")
                continue  # Skip lines that don't match the expected analogy format

            # Extract words from the matched groups
            word1, word2_target, target = match.groups()

            # Retrieve the word vectors for the three words (X, Y, A) from the model
            vec1 = model[word1]  # Vector for X
            vec2 = model[word2_target]  # Vector for Y
            vec_target = model[target]  # Vector for A

            # Perform the analogy calculation: B = Y - X + A
            analogy_vector = vec_target + (vec2 - vec1)

            # Find the most similar word to the resulting vector
            result = model.similar_by_vector(analogy_vector, topn=1)
            result_word = keep_ascii_and_digits(result[0][0])  # Clean the result word

            # Print the analogy result
            print(f"Target word for analogy '{target}' ({word2_target} - {word1} + {target}): {result_word}")
            
            # Accumulate the result word into the 'flag' variable
            flag += result_word

        except KeyError as e:
            # Handle the case where a word is not found in the model
            print(f"Word not found in model: {e}")

# After processing all lines, print the accumulated flag
print(f"[+] Flag: {flag}")

