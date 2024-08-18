# Error Rates : Out of the box

### Tools Used: Pytesseract, OpenCV, Pillow
#### Is text preprocessed? : Yes.

The following tests have been conducted over a limited number of filed with varying conditions such as plain text, colored text, skewed text,
handwritten text, different lighting conditions etc.

PIL and OpenCV are used to manipulate the images and preprocess them in order to increase the accuracy with which pytesseract ocr
can extract the text.


## Hindi


| **Ground Truth File**   | **OCR Output File**   | **CER (%)** | **WER**  | **Classification** |
|-------------------------|------------------------|-------------|----------|---------------------|
| images/hin/image_gt     | images/hin/image_out   | 35.96       | 2.9709   | Average             |
| images/hin/none_gt      | images/hin/none_out    | 10.48       | 0.3333   | Good                |
| images/hin/print_gt     | images/hin/print_out   |  6.69       | 0.2857   | Good                |
| images/hin/simple_gt    | images/hin/simple_out  | 11.76       | 0.0000   | Good                |
| **Average**             |                        | **16.72**   | **0.8975** |                     |
| **Median**              |                        | **11.76**   | **0.3095** |                     |




## Sanskrit

### Text Preprocessing : NO

Good: CER ≤ 20%
Average: 20% < CER ≤ 50%
Bad: CER > 50%


| Ground Truth File      | OCR Output File       | CER (%)    | WER         | CER Category |
|------------------------|------------------------|------------|-------------|--------------|
| images/san/nonemb_gt   | images/san/nonemb_out  | 89.58%     | 7.6693      | Bad          |
| images/san/sansk_gt    | images/san/sansk_out   | **340.25%**| **30.0000** | Bad          |
| images/san/sc2_gt      | images/san/sc2_out     | 63.92%     | 31.0000     | Bad          |
| images/san/simple_gt   | images/san/simple_out  | 19.51%     | 3.2000      | Good         |
| images/san/skew_gt     | images/san/skew_out    | 91.83%     | 39.9091     | Bad          |
| images/san/t1_gt       | images/san/t1_out      | 15.22%     | 9.3333      | Good         |
| images/san/t2_gt       | images/san/t2_out      | 68.18%     | 27.0000     | Bad          |
| images/san/t3_gt       | images/san/t3_out      | 96.12%     | 59.5000     | Bad          |
| images/san/t4_gt       | images/san/t4_out      | 81.84%     | 44.1250     | Bad          |
| images/san/t5.gt       | images/san/t5_out      | 80.38%     | 31.6250     | Bad          |
| images/san/t6_gt       | images/san/t6_out      | 51.51%     | 9.8889      | Bad          |
| images/san/t7_gt       | images/san/t7_out      | 26.22%     | 10.5294     | Average      |
| **Average**            |                        | **81.82%** | **25.8128** |              |
| **Median**             |                        | **75.01%** | **18.7647** |              |


*(The error in calculating CER occurs because of a very large amount of misrecognised characters. This has occured in this case due to lack of
preprocessing the original image, which is in handwritter format.



### Text Preprocessing : YES

| Ground Truth File      | OCR Output File         | CER (%)   | WER         | CER Category |
|------------------------|--------------------------|-----------|-------------|--------------|
| images/san/nonemb_gt   | images/san/nonemb_pp_out | 87.02%    | 7.4488      | Bad          |
| images/san/sansk_gt    | images/san/sansk_pp_out  | 78.62%    | 6.8333      | Bad          |
| images/san/sc2_gt      | images/san/sc2_pp_out    | 62.11%    | 30.1250     | Bad          |
| images/san/simple_gt   | images/san/simplepp_pp_out | 19.51%   | 3.0000      | Good         |
| images/san/skew_gt     | images/san/skew_pp_out   | 85.01%    | 36.9091     | Bad          |
| images/san/t1_gt       | images/san/t1_pp_out     | 17.93%    | 11.0000     | Good         |
| images/san/t2_gt       | images/san/t2_pp_out     | 37.19%    | 15.0000     | Average      |
| images/san/t3_gt       | images/san/t3_pp_out     | 95.64%    | 59.0500     | Bad          |
| images/san/t4_gt       | images/san/t4_pp_out     | 84.14%    | 45.2500     | Bad          |
| images/san/t5.gt       | images/san/t5_pp_out     | 81.33%    | 31.8750     | Bad          |
| images/san/t6_gt       | images/san/t6_pp_out     | 60.55%    | 11.7222     | Bad          |
| images/san/t7_gt       | images/san/t7_pp_out     | 32.65%    | 13.2353     | Average      |
| **Average**            |                          | **60.76%**| **23.3095** |              |
| **Median**             |                          | **69.58%**| **15.0000** |              |


## Comparing Error rates pre and post processing


![san](https://github.com/user-attachments/assets/d825dc86-da8e-46cd-91a7-b18ed33aa4d7)

