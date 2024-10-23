import cv2
from cv2.gapi import BGR2Gray
import numpy as np

img = cv2.imread('../static/real_car.jpeg')
grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

_, th = cv2.threshold(grey, 127, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

contours, hierarchy = cv2.findContours(th, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0, 255, 0), 2)

cv2.imwrite('../out/th_contour.jpeg', img)
