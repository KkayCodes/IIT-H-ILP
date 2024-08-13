# Error Rates : Out of the box

### Tools Used: Pytesseract, OpenCV, Pillow
#### Is text preprocessed? : Yes.

The following tests have been conducted over a limited number of filed with varying conditions such as plain text, colored text, skewed text,
handwritten text, different lighting conditions etc.

PIL and OpenCV are used to manipulate the images and preprocess them in order to increase the accuracy with which pytesseract ocr
can extract the text.


## Hindi

| Ground Truth File      | OCR Output File       | CER                       | WER                       |
|------------------------|------------------------|---------------------------|---------------------------|
| images/hin/image_gt    | images/hin/image_out   | 🚩 0.3596                 | 🚩 2.9709                 |
| images/hin/none_gt     | images/hin/none_out    | 🚩 0.1048                 | 🚩 0.3333                 |
| images/hin/print_gt    | images/hin/print_out   | 🚩 0.0669                 | 🚩 0.2857                 |
| images/hin/simple_gt   | images/hin/simple_out  | ✨ 0.1176                 | ✨ 0.0000                 |
| **Average**            |                        | **0.1622**               | **0.8975**               |
