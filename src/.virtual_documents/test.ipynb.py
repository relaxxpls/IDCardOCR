import matplotlib.pyplot as plt
from PIL import Image
import pytesseract
import cv2
import re
from scipy.ndimage import rotate


dob = re.compile("([0-9]{2}/[0-9]{2}/[0-9]{4})")
PAN_id = re.compile("([A-Z]{5}[0-9]{4}[A-Z]{1})")
r = re.compile("([A-Z]{5}[0-9]{4}[A-Z]{1})|([0-9]{2}/[0-9]{2}/[0-9]{4})")

margin = 10


def disp_img(img):
    plt.figure(figsize=(6,4))
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


def preprocess(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return img


def get_dob():
    return dob


def identify_pan_card(img):
    # Preprocess
    img = preprocess(img)
    
    # Extract text
    data = pytesseract.image_to_data(img, output_type='dict')
    
    # Clean text
    details = [(id, text) for id, text in enumerate(data['text']) if r.match(text)]
    
    # Mark locations on image
    for (id, text) in details:
        left = data['left'][id] - margin
        top = data['top'][id] - margin
        width = data['width'][id] + 2*margin
        height = data['height'][id] + 2*margin
        cv2.rectangle(img, (left, top), (left+width, top+height), (0, 0, 255), 4)
    
    return img, details


img = cv2.imread('dataset/PanTest_2.jpg') # BGR format
disp_img(img)

img_marked, details = identify_pan_card(img)
disp_img(img_marked)



