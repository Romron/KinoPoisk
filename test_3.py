import cv2
import numpy as np
# import video

if __name__ == '__main__':
    def nothing(*arg):
        pass

cv2.namedWindow( "settings" ) # создаем окно настроек

# cap = video.create_capture(0)
# создаем 6 бегунков для настройки начального и конечного цвета фильтра
cv2.createTrackbar('h1', 'settings', 0, 255, nothing)
cv2.createTrackbar('s1', 'settings', 0, 255, nothing)
cv2.createTrackbar('v1', 'settings', 0, 255, nothing)
cv2.createTrackbar('h2', 'settings', 255, 255, nothing)
cv2.createTrackbar('s2', 'settings', 255, 255, nothing)
cv2.createTrackbar('v2', 'settings', 255, 255, nothing)
crange = [0,0,0, 0,0,0]

while True:
    # flag, img = cap.read()
    img = cv2.imread(r"test.jpg")
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV )
 
    # считываем значения бегунков
    h1 = cv2.getTrackbarPos('h1', 'settings')
    s1 = cv2.getTrackbarPos('s1', 'settings')
    v1 = cv2.getTrackbarPos('v1', 'settings')
    h2 = cv2.getTrackbarPos('h2', 'settings')
    s2 = cv2.getTrackbarPos('s2', 'settings')
    v2 = cv2.getTrackbarPos('v2', 'settings')

    # # формируем начальный и конечный цвет фильтра
    # h_min = np.array((h1, s1, v1), np.uint8)
    # h_max = np.array((h2, s2, v2), np.uint8)

    # # накладываем фильтр на кадр в модели HSV
    # thresh_1 = cv2.inRange(hsv, h_min, h_max)

    # hsv_img_saturation = hsv[:,:,1] 
    # connectivity = s1    
    # ret, thresh_2 = cv2.threshold(hsv_img_saturation, h1, h2, cv2.THRESH_BINARY_INV)

    # cv2.imshow('result_1', thresh_1) 
    # cv2.imshow('result_2', thresh_2) 


    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh_gray = cv2.threshold(gray_img, h1, h2, cv2.THRESH_BINARY_INV)


    cv2.imshow('gray_img',gray_img)
    cv2.imshow('thresh_gray',thresh_gray)



    ch = cv2.waitKey(5)
    if ch == 27:
        break

cv2.destroyAllWindows()