'''
	открыть картинку
	создать маску
		подобрать параметры
		убрать шум
	преобразования по маске
'''

import cv2
import numpy as np
import random


img = cv2.imread(r"test.jpg")
hsv_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV )

shape_hsv_img = np.shape(hsv_img)

height = int(shape_hsv_img[0]*0.85)
width = int(shape_hsv_img[1]*0.7)

h_img_zero = np.zeros(np.shape(hsv_img))
h_img_zero = hsv_img[height:,width:,:]

h_min = np.array((28, 28, 0))
h_max = np.array((255, 255, 255))

thresh = cv2.inRange(h_img_zero, (28, 28, 0), (255, 255, 255))

contours, hirerchy = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

cv2.drawContours(h_img_zero, contours, 1, (255,0,255), -3)

print(contours)
print('************************')
print(hirerchy)

cv2.imshow('3',h_img_zero)
# cv2.imshow('4',h_img_zero)


cv2.waitKey(0)
cv2.destroyAllWindows()