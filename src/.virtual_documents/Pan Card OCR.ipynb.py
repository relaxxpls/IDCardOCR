import matplotlib.pyplot as plt
from PIL import Image
import pytesseract
import cv2
import re
from scipy.ndimage import rotate


r = re.compile("([A-Z]{5}[0-9]{4}[A-Z]{1})|([0-9]{2}/[0-9]{2}/[0-9]{4})")    


def disp_img(img):
    plt.figure(figsize=(6,4))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

margin = 10
# x_margin, y_margin = 10, 10


img = cv2.imread('dataset/PanTest_1.jpg') # BGR format
disp_img(img)


img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
disp_img(img_gray)


img_blur = cv2.GaussianBlur(img_gray, (3, 3), 0)
disp_img(img_blur)


img_thresh = cv2.threshold(img_blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
disp_img(img_thresh)


kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
img_opening = cv2.morphologyEx(img_thresh, cv2.MORPH_OPEN, kernel, iterations=1)

disp_img(img_opening)


img_invert = 255 - img_opening
disp_img(img_invert)








data = pytesseract.image_to_data(img_gray, output_type='dict')

print(data.keys())
print('Detected Text:', data['text'])


bag = [(id, text) for id, text in enumerate(data['text']) if r.match(text)]
display(bag)


img_marked = img.copy()

for (id, text) in bag:
    left = data['left'][id] - margin
    top = data['top'][id] - margin
    width = data['width'][id] + 2*margin
    height = data['height'][id] + 2*margin
    cv2.rectangle(img_marked, (left, top), (left+width, top+height), (0, 0, 255), 4)

disp_img(img_marked)



