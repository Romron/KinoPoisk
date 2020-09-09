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

img = cv2.imread(r"test_img/test_1.jpg")
template = cv2.imread(r"test_img/templ.jpg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray_img, 88, 255, cv2.THRESH_BINARY_INV)
mask = ~mask

result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
print("max_loc",max_loc)

mask[0:max_loc[1],:] = 0
mask[:,0:max_loc[0]] = 0

dst_TELEA = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
cv2.imshow('dst_TELEA',dst_TELEA)

cv2.waitKey(0)
cv2.destroyAllWindows()
