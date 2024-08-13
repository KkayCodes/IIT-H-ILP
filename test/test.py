import pytesseract
from PIL import Image
import cv2 as cv
import numpy as np

def preProcess(imagePath):
    # Load the image
    image = cv.imread(imagePath)
    
    if image is None:
        raise ValueError(f"Image at path {imagePath} could not be loaded.")
    
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

# Path to the image file
imagePath = r'images/tam/tam1.png'

# Extract text from the image
text = extractText(imagePath)

# Print the extracted text
print(text)
