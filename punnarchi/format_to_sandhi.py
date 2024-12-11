import re
import pandas as pd

# Define Tamil Sandhi splitting rules (using the provided rules)
sandhi_split_rules = [
    (r"(?<=\w)க்(?=\w)", "க + க்"),
    (r"(?<=\w)ஞ(?=\w)", "ஞ் + ஞ்"),
    (r"(?<=\w)ரு(?=\w)", "று + ரு"),
    (r"(?<=\w)க்கு(?=\w)", "க + க்கு"),
    (r"(?<=\w)செ(?=\w)", "சே + செ"),
    (r"(?<=\w)ள்(?=\w)", "ள + ள்"),
    (r"(?<=\w)ய(?=\w)", "ய் + ய"),
    (r"(?<=\w)ந்(?=\w)", "ன் + ந்"),
    (r"(?<=\w)சா(?=\w)", "சா + சா"),
]

# Function to split Sandhi words
def split_sandhi_word(word, rules):
    """S
    Splits a Tamil Sandhi word into its components based on rules.
    :param word: The compound word to split.
    :param rules: List of Sandhi splitting rules.
    :return: Split components as a string.
    """
    for pattern, replacement in rules:
        if re.search(pattern, word):
            return re.sub(pattern, replacement, word)
    return word  # Return the original word if no rules match

# Read input words from a CSV file
input_file = '/home/kkay/IIT-H/OCR/ILP-OCR/punnarchi/sandhi_words_from_oscar_tamil.csv'  # Replace with your CSV file name
output_file = "split_sandhi_words.csv"

try:
    df_input = pd.read_csv(input_file)
    sandhi_words = df_input["Sandhi Words"].tolist()  # Assuming the column is named 'Sandhi Words'
except FileNotFoundError:
    print(f"File not found: {input_file}")
    exit()
except KeyError:
    print(f"The input file must contain a column named 'Sandhi Words'.")
    exit()

# Clean words to remove unwanted characters like quotes, commas, etc.
cleaned_words = [word.strip().strip('\".,?') for word in sandhi_words]

# Process the words and prepare results
split_results = []
for word in cleaned_words:
    split_result = split_sandhi_word(word, sandhi_split_rules)
    split_results.append({"Original Word": word, "Split Form": split_result})

# Save results to a new CSV file
df_output = pd.DataFrame(split_results)
df_output.to_csv(output_file, index=False, encoding="utf-8")

print(f"Sandhi split results saved to {output_file}")
print("Sample Results:")
print(df_output.head())
