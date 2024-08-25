import difflib
import re

# def normalize_text(text):
#     # Remove any zero-width spaces and extra spaces
#     return re.sub(r'[\u200C\u200D\s]+', ' ', text).strip()

def calculate_cer(ground_truth, output_text):
    seqmatcher = difflib.SequenceMatcher(None, ground_truth, output_text)
    total_chars = len(ground_truth)
    errors = total_chars - seqmatcher.get_matching_blocks()[0][2]
    return errors / total_chars

def calculate_wer(ground_truth, output_text):
    ground_truth_words = ground_truth.split()
    output_text_words = output_text.split()
    seqmatcher = difflib.SequenceMatcher(None, ground_truth_words, output_text_words)
    total_words = len(ground_truth_words)
    errors = total_words - seqmatcher.get_matching_blocks()[0][2]
    return errors / total_words


with open(r'images/tam/print_gt.txt', 'r', encoding='utf-8') as f:
    gt_text = f.read().strip()

with open(r'images/tam/print_out.txt', 'r', encoding='utf-8') as f:
    ocr_text = f.read().strip()


cer = calculate_cer(gt_text, ocr_text)
wer = calculate_wer(gt_text, ocr_text)

print("CER:", cer)
print("WER:", wer)