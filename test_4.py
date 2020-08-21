import cv2









def main():
	structure_ArrImg = cv2.imread('image.jpg')
	cv2.imshow('window_1',structure_ArrImg)
	cv2.waitKey(0)









if __name__ == '__main__':
	main()