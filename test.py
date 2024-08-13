import pytesseract
from PIL import Image
import cv2 as cv
import numpy as np
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

def preProcess(imagePath):
    # Load the image
    image = cv.imread(imagePath)
    
    if image is None:
        raise ValueError(f"{AnsiColors.FAIL}Error: Image at path {imagePath} could not be loaded.{AnsiColors.ENDC}")
    
    # Convert the image to grayscale
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    
    # Apply binary thresholding to segment out the text
    _, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    
    return binary

def extractText(imagePath):
    # Preprocess the image
    binary = preProcess(imagePath)
    
    # Convert binary image back to PIL format
    pil_image = Image.fromarray(binary)
    
    # Perform OCR using Tesseract
    text = pytesseract.image_to_string(pil_image, lang='tam')
    
    return text

def main():
    # Ask user for the relative path to the image file
    imagePath = input(f"{AnsiColors.OKBLUE}Enter the relative path to the image file:{AnsiColors.ENDC} ").strip()
    
    # Ask user for the output file name
    outputFileName = input(f"{AnsiColors.OKBLUE}Enter the name of the output file (e.g., output.txt):{AnsiColors.ENDC} ").strip()
    
    # Extract text from the image
    try:
        extracted_text = extractText(imagePath)
    except ValueError as e:
        print(e)
        return
    
    # Write the extracted text to the output file
    try:
        with open(outputFileName, 'w') as file:
            file.write(extracted_text)
        print(f"{AnsiColors.OKGREEN}Text successfully written to {outputFileName}.{AnsiColors.ENDC}")
    except IOError as e:
        print(f"{AnsiColors.FAIL}Error writing to file: {e}{AnsiColors.ENDC}")

if __name__ == "__main__":
    main()
