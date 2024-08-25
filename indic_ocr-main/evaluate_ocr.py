import Levenshtein as lev
import re

# Normalize text by removing extra spaces and ZWJ characters
def normalize_text(text):
    # Remove any zero-width spaces and extra spaces
    return re.sub(r'[\u200C\u200D\s]+', ' ', text).strip()

def calculate_cer(gt_text, ocr_text):
    return lev.distance(gt_text, ocr_text) / len(gt_text)

def calculate_wer(gt_text, ocr_text):
    gt_words = gt_text.split()
    ocr_words = ocr_text.split()
    return lev.distance(" ".join(gt_words), " ".join(ocr_words)) / len(gt_words)

# Load and normalize ground truth and OCR output
with open(r'images/tam/print_gt.txt', 'r', encoding='utf-8') as f:
    gt_text = normalize_text(f.read().strip())

with open(r'images/tam/print_out.txt', 'r', encoding='utf-8') as f:
    ocr_text = normalize_text(f.read().strip())

# Calculate CER and WER
cer = calculate_cer(gt_text, ocr_text)
wer = calculate_wer(gt_text, ocr_text)

print(f'Character Error Rate (CER): {cer:.4f}')
print(f'Word Error Rate (WER): {wer:.4f}')
