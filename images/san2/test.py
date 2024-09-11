import pytesseract
from PIL import Image
import os

# Correctly set Tesseract command and path
pytesseract.pytesseract.tesseract_cmd = r'//home/kkay/IIT-H/OCR/ILP-OCR/indic_ocr-main/tessdata'
os.environ['TESSDATA_PREFIX'] = r'/home/kkay/IIT-H/OCR/ILP-OCR/indic_ocr-main/tessdata'

def extractText(imagePath):
    pil_image = Image.open(imagePath)
    custom_config = r'--tessdata-dir "/home/kkay/IIT-H/OCR/ILP-OCR/indic_ocr-main/tessdata"'
    text = pytesseract.image_to_string(pil_image, lang='san_best', config=custom_config)
    return text
