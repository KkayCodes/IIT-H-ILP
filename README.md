# ILP-OCR

### Goal: To create an accurate and tangible model that is adaptable for processing indic languages by making use of Optical Character Recognition techniques.

## How to use the files

**1. out.py**

This is a script that takes in the relative path as the input and writes the extracted text to the user specified file. It contains pre-processing techniques through OpenCV.

```bash
python3 out.py
```

**2. eval.py**

This script takes in the ground truth and output files as user inputs and prints Character Error Rate(CER) and Word Error Rate(WER) using levenshtein distance to calculate
the above.

```bash
python3 eval.py
```
