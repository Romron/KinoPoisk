import numpy as np
import cv2

def nothing(*arg):
    pass


# cv2.namedWindow( "settings" ) # создаем окно настроек

# cv2.createTrackbar('h1', 'settings', 0, 255, nothing)
# cv2.createTrackbar('s1', 'settings', 0, 255, nothing)

while True:

	h1 = cv2.getTrackbarPos('h1', 'settings')
	s1 = cv2.getTrackbarPos('s1', 'settings')
	img = cv2.imread('image.jpg')
	hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	image_saturation = hsv_img[:,:,1]
	# ret, thresh_s = cv2.threshold(image_saturation, h1, s1, cv2.THRESH_BINARY_INV)
	ret, thresh_s = cv2.threshold(image_saturation, 40, 255, cv2.THRESH_BINARY_INV)

	edged = cv2.Canny(thresh_s, 10, 250)
	
	kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
	closed = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)


	cv2.imshow("Image", closed)

	ch = cv2.waitKey(5)
	if ch == 27:
		break