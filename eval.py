import Levenshtein as lev
import os

# Define ANSI color codes for formatting
class AnsiColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def calculate_cer(gt_text, ocr_text):
    """Calculate the Character Error Rate (CER)."""
    return lev.distance(gt_text, ocr_text) / len(gt_text) if len(gt_text) > 0 else 0

def calculate_wer(gt_text, ocr_text):
    """Calculate the Word Error Rate (WER)."""
    gt_words = gt_text.split()
    ocr_words = ocr_text.split()
    return lev.distance(" ".join(gt_words), " ".join(ocr_words)) / len(gt_words) if len(gt_words) > 0 else 0

def colorize_text(text, cer, wer):
    """Colorize the output based on CER and WER values."""
    if cer < 0.05 and wer < 0.05:
        color = AnsiColors.OKGREEN
    elif cer < 0.2 and wer < 0.2:
        color = AnsiColors.WARNING
    else:
        color = AnsiColors.FAIL
    
    return f"{color}{text}{AnsiColors.ENDC}"

def main():
    # Define the header for the Markdown table
    header = '| Ground Truth File      | OCR Output File       | CER         | WER         |\n'
    separator = '|------------------------|------------------------|-------------|-------------|\n'

    # Open the Markdown file in append mode
    with open('eval_out.md', 'a', encoding='utf-8') as error_file:
        # Write the header if the file is empty
        if os.stat('eval_out.md').st_size == 0:
            error_file.write(header)
            error_file.write(separator)
        
        while True:
            try:
                # Ask user for the paths to the ground truth and OCR output files
                gt_file_path = input(f"{AnsiColors.OKBLUE}Enter the relative path to the ground truth file (e.g., ground_truth.txt):{AnsiColors.ENDC} ").strip()
                ocr_file_path = input(f"{AnsiColors.OKBLUE}Enter the relative path to the OCR output file (e.g., ocr_output.txt):{AnsiColors.ENDC} ").strip()

                # Check if files exist
                if not os.path.exists(gt_file_path):
                    print(f"{AnsiColors.FAIL}Error: Ground truth file not found.{AnsiColors.ENDC}")
                    continue
                if not os.path.exists(ocr_file_path):
                    print(f"{AnsiColors.FAIL}Error: OCR output file not found.{AnsiColors.ENDC}")
                    continue

                # Load ground truth and OCR output
                with open(gt_file_path, 'r', encoding='utf-8') as f:
                    gt_text = f.read().strip()

                with open(ocr_file_path, 'r', encoding='utf-8') as f:
                    ocr_text = f.read().strip()

                # Calculate CER and WER
                cer = calculate_cer(gt_text, ocr_text)
                wer = calculate_wer(gt_text, ocr_text)

                # Print results with color coding
                cer_text = f'Character Error Rate (CER): {cer:.4f}'
                wer_text = f'Word Error Rate (WER): {wer:.4f}'
                
                print(colorize_text(cer_text, cer, wer))
                print(colorize_text(wer_text, cer, wer))

                # Format the output as a Markdown table row
                row = f"| {gt_file_path:<22} | {ocr_file_path:<22} | {cer:<11.4f} | {wer:<11.4f} |\n"
                
                # Write the formatted row to the Markdown file
                error_file.write(row)
                error_file.flush()  # Ensure the data is written to the file immediately

            except EOFError:
                print("\nExiting the loop.")
                break
            except Exception as e:
                print(f"{AnsiColors.FAIL}An unexpected error occurred: {e}{AnsiColors.ENDC}")

if __name__ == "__main__":
    main()
