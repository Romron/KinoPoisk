
'''
	открыть картинку
	создать маску
		подобрать параметры
		убрать шум
	преобразования по маске
'''

import cv2
import numpy as np


img = cv2.imread(r"IMG/posters/1060511_1.jpeg")
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )

# cv2.imshow('1',img)
# cv2.imshow('2',hsv_img)



cv2.waitKey(0)
cv2.destroyAllWindows()
