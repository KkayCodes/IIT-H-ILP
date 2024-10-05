import pytesseract
from PIL import Image
import cv2 as cv

def preProcess(imagePath):
    image = cv.imread(imagePath)
    if image is None:
        raise ValueError(f"Error: Image at path {imagePath} could not be loaded.")
    
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    _, binary = cv.threshold(gray, 127, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    
    return binary, image

def extractText(imagePath):
    binary, original_image = preProcess(imagePath)
    contours, _ = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    extracted_text = []

    for contour in contours:
        x, y, w, h = cv.boundingRect(contour)
        if w > 5 and h > 5:  
            roi = original_image[y:y + h, x:x + w]
            pil_image = Image.fromarray(cv.cvtColor(roi, cv.COLOR_BGR2RGB))
            custom_config = r'--psm 3'
            text = pytesseract.image_to_string(pil_image, lang='san', config=custom_config)
            extracted_text.append((text.strip(), (x, y, w, h)))
            cv.rectangle(original_image, (x, y), (x + w, y + h), (0, 255, 0), 2)  

    cv.imwrite('book.png', original_image)  
    return extracted_text

def main(imagePath, outputFileName):
    try:
        extracted_text = extractText(imagePath)
    except ValueError as e:
        print(e)
        return
    
    try:
        with open(outputFileName, 'w') as file:
            for text, bbox in extracted_text:
                file.write(f"{text}")
        print(f"Text successfully written to {outputFileName}.")
    except IOError as e:
        print(f"Error writing to file: {e}")
        

if __name__ == "__main__":
    main('/home/kkay/IIT-H/OCR/ILP-OCR/images/san/book.png', 'book_output.txt')  
