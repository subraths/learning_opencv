
import cv2

img = cv2.imread('../static/real_car.jpeg', 0)


ret, th = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

cv2.imwrite('../out/th_otsu.jpeg', th)

cv2.waitKey(0)
cv2.destroyAllWindows()
