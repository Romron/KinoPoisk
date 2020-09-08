import numpy as np
import os
import random
import cv2
import cv

# Рабочи вариант с ползунками:
# def nothing(*arg):
#     pass


# cv2.namedWindow( "result" ) # создаем главное окно
# cv2.namedWindow( "settings" ) # создаем окно настроек
# hight = cv2.createTrackbar('hight', 'settings', 0, 255, nothing)
# low = cv2.createTrackbar('low', 'settings', 0, 255, nothing)


# image = cv2.imread(r"IMG/posters/1060511_1.jpeg")
# row,col, chen = image.shape
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# while True:

# 	# считываем значения бегунков
# 	H = cv2.getTrackbarPos('hight', 'settings')
# 	L = cv2.getTrackbarPos('low', 'settings')
# 	ret, curr_mask_2 = cv2.threshold(gray_image,L, H, cv2.THRESH_BINARY_INV)

# 	cv2.imshow("result",curr_mask_2)

# 	ch = cv2.waitKey(5)
# 	if ch == 27:
# 		break

# cv2.destroyAllWindows()



# image = cv2.imread(r"IMG/posters/1060511_1.jpeg")
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# ret, curr_mask_2 = cv2.threshold(gray_image,150, 200, cv2.THRESH_BINARY_INV)
# contours, hierarchy = cv2.findContours(curr_mask_2.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# for cnt in contours:
# 	rect = cv2.minAreaRect(cnt)  # пытаемся вписать прямоугольник
# 	box = cv2.boxPoints(rect)  # поиск четырех вершин прямоугольника
# 	box = np.int0(box)  # округление координат
# 	cv2.drawContours(gray_image, [box], -1, (255, 0, 0), 0)  # рисуем прямоугольник
# cv2.imshow('contours', gray_image)  # вывод обработанного кадра в окно
# print(len(contours))
# # cv2.drawContours(gray_image, contours, 200, (255, 255, 255),5, cv2.LINE_8, hierarchy, 2)
# # cv2.imshow('contours', gray_image)

# # cv2.imshow("result",curr_mask_2)
# # cv2.imshow("result",сontour)
# cv2.waitKey(0)

def coloured_image_to_edge_mark(coloured_image):
   image_sum = coloured_image[:,:,0] + coloured_image[:,:,1] + coloured_image[:,:,2]
   mask = image_sum > 0
   return mask

def make_random_colour_map_with_stats(stats, pop_thresh = 0):
    n = len(stats)
    colour_map = np.zeros( [n, 3], dtype=np.uint8)	# Возвращает новый массив заданной формы и типа, заполненный нулями
    for i in range(n):
        print('stats[',i,']  ',stats[i])	# test

        if ( (pop_thresh != 0) and (stats[i][4] < pop_thresh) ) or  (i == 0):		# в stats[0] находиться служебная информация
             colour_map[i] = [0,0,0]                            # make small regions and region 0 (background) black
        else:
            for j in range(3):
                colour_map[i,j] = 1 + random.randint(0,254)     # big regions are a non-zero random colou
        print('colour_map[',i,']  ',colour_map[i])		#test
    return colour_map

def rgb_to_hsv(im):
    return cv2.cvtColor(im, cv2.COLOR_BGR2HSV)	#  для преобразования изображения из цветового RGB в HSV

def display_and_output_image(name, structure_ArrImg):
    cv2.imshow(name,structure_ArrImg)		# отображаю изображения в окне. name - имя окна, structure_ArrImg - растркартинки. Окно автоматически подгоняется под размер изображения
    file_name = os.path.join( "C:\\Users\\david\\Desktop\\", name + ".jpg")
    cv2.imwrite(file_name,structure_ArrImg)	# сохранения изображения на любом устройстве хранения. Сохранит изображение в соответствии с указанным форматом в текущем рабочем каталоге.

def create_letter_mask(image_saturation):
    """
    https://stackoverflow.com/questions/35854197/how-to-use-opencvs-connected-components-with-stats-in-python

    threshold saturation to detect letters (low saturation)
    find big connected components (small connected components are noise)

	пороговая насыщенность для обнаружения букв (низкая насыщенность)
    найти большие связанные компоненты (маленькие связанные компоненты - это шум)

    """
    connectivity = 4		# связь(?)
    ret, thresh_s = cv2.threshold(image_saturation, 42, 255, cv2.THRESH_BINARY_INV)  # 50 too high, 25 too low	пороговая сигментация изображения т.е. в результате получаю белые буквы на чёрном фоне
    display_and_output_image("create_letter_mask_1",thresh_s) # test
    output = cv2.connectedComponentsWithStats(thresh_s, connectivity, cv2.CV_32S)	# поиска связанных компонентов возвращает кортеж номеров компонентов и изображение с метками для компонентов статистику о каждом компоненте и их центроидах.
    blob_image = output[1]	# здесь находиться изображение с метками для компонентов (??)
    stats = output[2]	# здесь находиться статистика о каждом компоненте и их центроидах (??)
    
    вывести массив на печать поэлементно




    pop_thresh = 170
    big_blob_colour_map = make_random_colour_map_with_stats(stats, pop_thresh)	# возвращает маску случайного цвета используя статистику для большого региона(??)
    all_blob_colour_map = make_random_colour_map_with_stats(stats)	# возвращает маску случайного цвета используя статистику для всех регионов(?????)
    big_blob_coloured_image = big_blob_colour_map[blob_image]                       # output
    all_blob_coloured_image = all_blob_colour_map[blob_image]                       # output
    display_and_output_image("big_blob_coloured_image", big_blob_coloured_image)
    display_and_output_image("all_blob_coloured_image", all_blob_coloured_image)
    letter_mask = coloured_image_to_edge_mark(big_blob_coloured_image)
    return letter_mask




structure_ArrImg = cv2.imread(r"IMG/riba_pix_cropped.jpg")
print (structure_ArrImg.shape)
# display_and_output_image("image_1",structure_ArrImg)
hsv = rgb_to_hsv(structure_ArrImg)
# display_and_output_image("image_2",hsv) # test
image_saturation = hsv[:,:,1]
display_and_output_image("image_3",image_saturation) # test
letter_mask = create_letter_mask(image_saturation)
cv2.waitKey(0)