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
h_templ, w_templ, deth = np.shape(template)

print(np.shape(img))
print(np.shape(template))

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(gray_img, 88, 255, cv2.THRESH_BINARY_INV)
mask = ~mask

# h = np.shape(mask)[0] - 40
# w = np.shape(mask)[1] - 155

# mask[0:370,:] = 0
# mask[:,0:420] = 0
# print(h,w)

# mask[0:h,:] = 0
# mask[:,0:w] = 0
# dst_TELEA = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
# cv2.imshow('dst_TELEA',dst_TELEA)

# print(np.shape(mask))
# cv2.imshow('shape',mask)

methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
n_window = 0
for meth in methods:

	img_n = img.copy()
	method = eval(meth)
	result = cv2.matchTemplate(img, template, method)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

	print('min_val',min_val,'max_val',max_val,'min_loc',min_loc,'max_loc',max_loc)

	# If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
	if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
	    top_left = min_loc
	else:
	    top_left = max_loc
	bottom_right = (top_left[0] + w_templ, top_left[1] + h_templ)

	cv2.rectangle(img_n,top_left, bottom_right, 255, 2)

	n_window = str(n_window) 
	cv2.imshow(n_window,img_n)
	n_window = int(n_window)
	n_window += 1


# result = cv2.matchTemplate(img, template, 'cv2.TM_CCORR_NORMED')
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
# top_left = max_loc
# bottom_right = (top_left[0] + w_templ, top_left[1] + h_templ)


cv2.waitKey(0)
cv2.destroyAllWindows()
