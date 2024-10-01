import cv2

image_path = 'images/san/sansk.jpg'
image = cv2.imread(image_path)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, binary_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY_INV)

contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    if w > 30 and h > 30:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

output_path = 'sanskrit_text_bounding_boxes.png'
cv2.imwrite(output_path, image)

print(f"Image saved with bounding boxes as {output_path}")
