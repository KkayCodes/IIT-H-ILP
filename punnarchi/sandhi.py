from datasets import load_dataset
import re
import pandas as pd

# Define all Tamil Sandhi rules (This is just a sample; you may need to add more rules based on your corpus)
sandhi_rules = [
    (r"(?<=\w)க்(?=\w)", "க"),
    (r"(?<=\w)ஞ(?=\w)", "ஞ்"),
    (r"(?<=\w)ரு(?=\w)", "று"),
    (r"(?<=\w)க்கு(?=\w)", "க"),
    (r"(?<=\w)செ(?=\w)", "சே"),
    (r"(?<=\w)ள்(?=\w)", "ள"),
    (r"(?<=\w)ய(?=\w)", "ய்"),
    (r"(?<=\w)ந்(?=\w)", "ன்"),
    (r"(?<=\w)சா(?=\w)", "சா"),  # Add as many Tamil Sandhi rules as necessary
    # Add more based on Tamil Sandhi transformations
]

# Load a small portion of the OSCAR dataset for Tamil (1% of the dataset)
print("Loading dataset...")
dataset = load_dataset("oscar-corpus/OSCAR-2201", language="ta", split="train[:1000]")

# Function to identify Sandhi words in a text based on the rules
def identify_sandhi_words(text, rules):
    """
    Identify words with Sandhi transformations in a given text.
    :param text: A document or text from the dataset.
    :param rules: List of Sandhi rules.
    :return: List of words with Sandhi transformations.
    """
    sandhi_words = []
    words = text.split()
    for word in words:
        for pattern, replacement in rules:
            if re.search(pattern, word):
                sandhi_words.append(word)
                break
    return sandhi_words

# Log for processing start
print("Processing dataset...")

# Process the dataset and collect Sandhi words
all_sandhi_words = []
for idx, doc in enumerate(dataset):
    if idx % 100 == 0:  # Log progress every 100 documents
        print(f"Processing document {idx + 1}/{len(dataset)}...")
    
    sandhi_words = identify_sandhi_words(doc["text"], sandhi_rules)
    all_sandhi_words.extend(sandhi_words)

print("Dataset processing complete.")

# Save Sandhi words to a CSV file
output_file = "sandhi_words_from_oscar_tamil.csv"
print(f"Saving Sandhi words to {output_file}...")
df_sandhi_words = pd.DataFrame(all_sandhi_words, columns=["Sandhi Words"])
df_sandhi_words.to_csv(output_file, index=False, encoding="utf-8")

# Final log message
print(f"Sandhi words extraction complete. Data saved to {output_file}")

# Print some results (First 5 Sandhi words)
print("Sample Sandhi Words Extracted:")
print(df_sandhi_words.head())
