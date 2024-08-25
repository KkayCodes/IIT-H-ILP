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
    
    return image, binary

def extractText(imagePath):
    # Preprocess the image (original image and binary processed image)
    original_image, binary = preProcess(imagePath)
    
    # Convert binary image back to PIL format
    pil_image = Image.fromarray(binary)
    
    # Perform OCR using Tesseract with -psm 6 and best model
    custom_config = r'--psm 6'
    text = pytesseract.image_to_string(pil_image, lang='san_best', config=custom_config)
    
    return original_image, text

def drawBoundingBoxes(imagePath, outputImagePath):
    # Load the original image
    original_image, binary = preProcess(imagePath)
    
    # Perform OCR and extract bounding box data
    h, w, _ = original_image.shape
    boxes = pytesseract.image_to_boxes(original_image)
    
    # Draw bounding boxes around each character
    for box in boxes.splitlines():
        box = box.split(' ')
        x, y, x2, y2 = int(box[1]), int(box[2]), int(box[3]), int(box[4])
        # OpenCV uses different origin (top-left), so we need to adjust y coordinates
        cv.rectangle(original_image, (x, h - y), (x2, h - y2), (0, 255, 0), 2)
    
    # Save the image with bounding boxes
    cv.imwrite(outputImagePath, original_image)
    print(f"{AnsiColors.OKGREEN}Bounding boxes saved to {outputImagePath}.{AnsiColors.ENDC}")

def main():
    while True:
        # Ask user for the relative path to the image file
        imagePath = input(f"{AnsiColors.OKBLUE}Enter the relative path to the image file:{AnsiColors.ENDC} ").strip()
        
        # Ask user for the output file name for text
        outputFileName = input(f"{AnsiColors.OKBLUE}Enter the name of the output text file (e.g., output.txt):{AnsiColors.ENDC} ").strip()

        # Ask user for the output file name for image with bounding boxes
        outputImageFileName = input(f"{AnsiColors.OKBLUE}Enter the name of the output image file with bounding boxes (e.g., output_image.jpg):{AnsiColors.ENDC} ").strip()

        # Extract text from the image
        try:
            original_image, extracted_text = extractText(imagePath)
        except ValueError as e:
            print(e)
            continue  # Continue the loop if an error occurs
        
        # Write the extracted text to the output file
        try:
            with open(outputFileName, 'w') as file:
                file.write(extracted_text)
            print(f"{AnsiColors.OKGREEN}Text successfully written to {outputFileName}.{AnsiColors.ENDC}")
        except IOError as e:
            print(f"{AnsiColors.FAIL}Error writing to file: {e}{AnsiColors.ENDC}")

        # Draw bounding boxes around the recognized text and save the image
        try:
            drawBoundingBoxes(imagePath, outputImageFileName)
        except ValueError as e:
            print(e)
            continue

if __name__ == "__main__":
    main()
