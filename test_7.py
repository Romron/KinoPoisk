import cv2
import numpy as np

img = cv2.imread(r"test.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)

edged = cv2.Canny(gray, 300, 450)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)

contours, hierarchy = cv2.findContours(closed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
total = 0


for c in contours:
    # аппроксимируем (сглаживаем) контур
    peri = cv2.arcLength(c, True)

    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    print('************')
    print(approx)
    print(len(approx))

    # если у контура 4 вершины, предполагаем, что это книга
    if len(approx) == 6:
	    cv2.drawContours(img, [approx], -1, (0, int(10+total*20), 0), 2)
	    total += 1



cv2.imshow('1',img)
cv2.waitKey(0)
cv2.destroyAllWindows()