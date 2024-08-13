import easyocr

reader = easyocr.Reader(['ta'])
result = reader.readtext('mk1jX.jpg')

print(result)