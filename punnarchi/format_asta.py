import pandas as pd

input_file = "split_sandhi_words.csv"
output_file = "formatted_sandhi_words.txt"

def convert_to_desired_format(split_form):
    split_parts = split_form.split(" + ")
    return "+".join(split_parts)

try:
    df_input = pd.read_csv(input_file)
except FileNotFoundError:
    print(f"File not found: {input_file}")
    exit()

with open(output_file, 'w', encoding='utf-8') as f:
    for _, row in df_input.iterrows():
        original_word = row["Original Word"]
        split_form = row["Split Form"]
        formatted_split = convert_to_desired_format(split_form)
        f.write(f"{original_word} => {formatted_split}\n")

print(f"Formatted results saved to {output_file}")
