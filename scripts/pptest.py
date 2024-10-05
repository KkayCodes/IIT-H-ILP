import cv2
import pytesseract
import numpy as np
from PIL import Image

# Grayscale and Binarization
image_path = '/home/kkay/IIT-H/OCR/ILP-OCR/images/san/book.png'
image = cv2.imread(image_path)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)

# Boundary Boxes
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if w > 5 and h > 5:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Save the image with bounding boxes
output_path = 'example.png'
cv2.imwrite(output_path, image)
print(f"Image saved with bounding boxes as {output_path}")

def extractTextFromBoxes(imagePath):
    # Load image
    image = cv2.imread(imagePath)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)

    # Find contours again (since it was done earlier)
    contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    extracted_text = ""
    
    # Iterate over the bounding box regions and extract text
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        if w > 10 and h > 10:
            # Crop the region of interest
            roi = binary_image[y:y + h, x:x + w]
            
            # Convert the ROI to a PIL Image for pytesseract
            roi_pil = Image.fromarray(roi)
            
            # Extract text from the ROI using Tesseract
            custom_config = r'--psm 3'
            text = pytesseract.image_to_string(roi_pil, lang='san', config=custom_config)
            extracted_text += text + "\n"

    return extracted_text

def main():
    imagePath = '/home/kkay/IIT-H/OCR/ILP-OCR/images/san/book.png'
    outputFileName = 'book_out.txt'
    
    try:
        extracted_text = extractTextFromBoxes(imagePath)
    except ValueError as e:
        print(e)
        return
    
    try:
        with open(outputFileName, 'w') as file:
            file.write(extracted_text)
        print(f"Text successfully written to {outputFileName}.")
    except IOError as e:
        print(f"Error writing to file: {e}")

if __name__ == "__main__":
    main()
