
'''
	открыть картинку
	создать маску
		подобрать параметры
		убрать шум
	преобразования по маске
		с помощью cv2.inpaint()
'''

import cv2
import numpy as np
import random

img = cv2.imread(r"IMG/posters/1060511_1.jpeg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh_gray = cv2.threshold(gray_img, 9, 255, cv2.THRESH_BINARY_INV)






cv2.imshow('gray_img',gray_img)
cv2.imshow('thresh_gray',thresh_gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
