from PIL import Image
import pytesseract
import cv2
import numpy as np

def preprocess_image(image_path):
    # Open image using PIL
    pil_img = Image.open(image_path).convert("RGB")
    
    # Convert PIL image to OpenCV format
    open_cv_image = np.array(pil_img)
    open_cv_image = open_cv_image[:, :, ::-1].copy()  # Convert RGB to BGR
    
    # Convert image to grayscale
    gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian blur
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply thresholding
    _, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    
    return thresh

def extract_text_from_image(image):
    # Use Pytesseract to extract text
    text = pytesseract.image_to_string(image)
    return text

def main():
    image_path = "sansk.jpg"  # Replace with your image file path
    
    # Preprocess the image
    preprocessed_image = preprocess_image(image_path)
    
    # Convert preprocessed image back to PIL format for Pytesseract
    pil_image = Image.fromarray(preprocessed_image)
    
    # Extract text from image
    extracted_text = extract_text_from_image(pil_image)
    
    print("Extracted Text:")
    print(extracted_text)

if __name__ == "__main__":
    main()
