def identify_pan_card(img):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    data = pytesseract.image_to_data(img_gray, output_type='dict')
    bag = [(id, text) for id, text in enumerate(data['text']) if r.match(text)]
    img_marked = img.copy()
    for (id, text) in bag:
        left = data['left'][id] - margin
        top = data['top'][id] - margin
        width = data['width'][id] + 2*margin
        height = data['height'][id] + 2*margin
        cv2.rectangle(img_marked, (left, top), (left+width, top+height), (0, 0, 255), 4)
    disp_img(img_marked)
