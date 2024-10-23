import cv2

img = cv2.imread('static/real_car.jpeg', cv2.IMREAD_GRAYSCALE)

threshold_value = 127
max_value = 255

ret, thresh = cv2.threshold(img, threshold_value, max_value, cv2.THRESH_BINARY)

cv2.imwrite('./out/original.jpeg',img)
cv2.imwrite('./out/thresholded.jpeg', thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
