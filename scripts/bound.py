import pytesseract
from PIL import Image
import cv2 as cv
import numpy as np
import os

class AnsiColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def preProcess(imagePath):
    image = cv.imread(imagePath)
    
    if image is None:
        raise ValueError(f"{AnsiColors.FAIL}Error: Image at path {imagePath} could not be loaded.{AnsiColors.ENDC}")
    
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    _, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    
    return image, binary

def extractText(imagePath, apply_preprocessing=True):
    if apply_preprocessing:
        original_image, binary = preProcess(imagePath)
        pil_image = Image.fromarray(binary)
    else:
        original_image = cv.imread(imagePath)
        if original_image is None:
            raise ValueError(f"{AnsiColors.FAIL}Error: Image at path {imagePath} could not be loaded.{AnsiColors.ENDC}")
        pil_image = Image.fromarray(cv.cvtColor(original_image, cv.COLOR_BGR2RGB))
    
    custom_config = r'--psm 3'
    text = pytesseract.image_to_string(pil_image, lang='san_best', config=custom_config)
    
    return original_image, text

def drawBoundingBoxes(imagePath, outputImagePath, apply_preprocessing=True):
    if apply_preprocessing:
        original_image, binary = preProcess(imagePath)
    else:
        original_image = cv.imread(imagePath)
        if original_image is None:
            raise ValueError(f"{AnsiColors.FAIL}Error: Image at path {imagePath} could not be loaded.{AnsiColors.ENDC}")
    
    h, w, _ = original_image.shape
    boxes = pytesseract.image_to_boxes(original_image)
    
    for box in boxes.splitlines():
        box = box.split(' ')
        x, y, x2, y2 = int(box[1]), int(box[2]), int(box[3]), int(box[4])
        cv.rectangle(original_image, (x, h - y), (x2, h - y2), (0, 255, 0), 2)
    
    cv.imwrite(outputImagePath, original_image)
    print(f"{AnsiColors.OKGREEN}Bounding boxes saved to {outputImagePath}.{AnsiColors.ENDC}")

def main():
    while True:
        imagePath = input(f"{AnsiColors.OKBLUE}Enter the relative path to the image file:{AnsiColors.ENDC} ").strip()
        
        outputImageFileName = input(f"{AnsiColors.OKBLUE}Enter the name of the output image file with bounding boxes (e.g., output_image.jpg):{AnsiColors.ENDC} ").strip()

        apply_preprocessing = input(f"{AnsiColors.OKBLUE}Would you like to apply preprocessing? (yes/no):{AnsiColors.ENDC} ").strip().lower() == 'yes'

        try:
            original_image, extracted_text = extractText(imagePath, apply_preprocessing)
            print(f"{AnsiColors.OKGREEN}Extracted Text:{AnsiColors.ENDC}\n{extracted_text}")
        except ValueError as e:
            print(e)
            continue
        
        try:
            drawBoundingBoxes(imagePath, outputImageFileName, apply_preprocessing)
        except ValueError as e:
            print(e)
            continue

if __name__ == "__main__":
    main()
