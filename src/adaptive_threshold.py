import cv2

img = cv2.imread('../static/real_car.jpeg', cv2.IMREAD_GRAYSCALE)

max_value = 255

adaptive_method = cv2.ADAPTIVE_THRESH_GAUSSIAN_C
threshold_type = cv2.THRESH_BINARY
block_size = 11
c = 2
thresh = cv2.adaptiveThreshold(img, max_value, adaptive_method, threshold_type, block_size, c)

cv2.imwrite('../out/adaptive_threshold.jpeg', thresh)
