
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

img = cv2.imread('../out/th_otsu.jpeg')
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh1 = cv2.threshold(grey, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

rect_kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (18,18))
dilation = cv2.dilate(thresh1, rect_kernal, iterations = 1)

contours, hierachy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

img2 = img.copy()

file = open('../out/recognized.txt', '+w')
file.write('')
file.close()

for cnt in contours:
    x, y, w, h = cv2.boundingRect(cnt)
    rect = cv2.rectangle(img2, (x,y), (x + w, y + h), (0, 255, 0), 2)

    croped = img2[y:y + h, x:x + w]

    file = open('../out/recognized.txt', 'a')
    text = pytesseract.image_to_string(croped)

    file.write(text)
    file.write('\n')
    file.close()
