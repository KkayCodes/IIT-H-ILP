import pytesseract
from pytesseract import Output
import cv2
import editdistance
import numpy as np

def calculate_wer(reference, hypothesis):
    ref_words = reference.split()
    hyp_words = hypothesis.split()
    distance = editdistance.eval(ref_words, hyp_words)
    return distance / len(ref_words)

def calculate_cer(reference, hypothesis):
    distance = editdistance.eval(reference, hypothesis)
    return distance / len(reference)

def ocr_with_psm(image_path, psm):
    config = f'--psm {psm}' 
    image = cv2.imread(image_path)  
    ocr_result = pytesseract.image_to_string(image, lang='san', config=config) 
    return ocr_result

def evaluate_psms(image_path, ground_truth):
    psm_results = {}

    for psm in range(0, 14): 
        ocr_result = ocr_with_psm(image_path, psm)
        
       
        wer = calculate_wer(ground_truth, ocr_result)
        cer = calculate_cer(ground_truth, ocr_result)

        psm_results[psm] = {'OCR_Result': ocr_result, 'WER': wer, 'CER': cer}
    
    return psm_results

def ground_truth_reader(ground_truth_path):
    with open(ground_truth_path, 'r+', encoding='utf-8') as f:
        gt = f.read()
    return gt

print(ground_truth_reader('images\\san2\\t1_gt'))

image_path = "images\\san2\\t1.jpeg" 
gt_path = 'images\\san2\\t1_gt'
ground_truth = ground_truth_reader(gt_path)
results = evaluate_psms(image_path, ground_truth)

for psm, metrics in results.items():
    print(f"PSM: {psm}")
    print(f"WER: {metrics['WER']:.4f}, CER: {metrics['CER']:.4f}")
    print(f"OCR Output: {metrics['OCR_Result']}\n")