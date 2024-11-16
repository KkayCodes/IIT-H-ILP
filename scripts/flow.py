import cv2
import numpy as np
import pytesseract
from matplotlib import pyplot as plt
from textblob import TextBlob

# Load and preprocess the image
img = cv2.imread('/home/kkay/IIT-H/OCR/ILP-OCR/book.png', 0)
denoised_img = cv2.fastNlMeansDenoising(img, None, 30, 7, 21)
_, binarised_img = cv2.threshold(denoised_img, 0, 255, cv2.THRESH_BINARY)

coords = np.column_stack(np.where(binarised_img > 0))
angle = cv2.minAreaRect(coords)[-1]
if angle < -45:
    angle = -(90 + angle)
else:
    angle = -angle
(h, w) = binarised_img.shape[:2]
center = (w // 2, h // 2)
M = cv2.getRotationMatrix2D(center, angle, 1.0)
rotated_img = cv2.warpAffine(binarised_img, M, (w, h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

resized_img = cv2.resize(rotated_img, (1024, 1024))
segmented_img = cv2.Canny(resized_img, 100, 200)

# OCR using PyTesseract
pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
custom_config = r'--oem 3 --psm 6 -l san'
text = pytesseract.image_to_string(segmented_img, config=custom_config)

# Post-processing: Spell check and punctuation fixing
blob = TextBlob(text)
corrected_text = blob.correct()
punctuation_fixed_text = corrected_text.replace("।", ".").replace("॥", "||")

# Display extracted and corrected text
print("Extracted Text: \n", text)
print("Corrected Text: \n", punctuation_fixed_text)
