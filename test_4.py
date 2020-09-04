import cv2
import numpy as np
import os
import random

def coloured_image_to_edge_mark(coloured_image):
   image_sum = coloured_image[:,:,0] + coloured_image[:,:,1] + coloured_image[:,:,2]
   mask = image_sum > 0
   return mask

def make_random_colour_map_with_stats(stats, pop_thresh = 0):
    n = len(stats)
    colour_map = np.zeros( [n, 3], dtype=np.uint8)  # Возвращает новый массив заданной формы и типа, заполненный нулями
    for i in range(n):
        if ( (pop_thresh != 0) and (stats[i][4] < pop_thresh) ) or  (i == 0):
             colour_map[i] = [0,0,0]                            # make small regions and region 0 (background) black
        else:
            for j in range(3):
                colour_map[i,j] = 1 + random.randint(0,254)     # big regions are a non-zero random colou
    return colour_map

def create_letter_mask(image_saturation):
    """
    https://stackoverflow.com/questions/35854197/how-to-use-opencvs-connected-components-with-stats-in-python

    threshold saturation to detect letters (low saturation)
    find big connected components (small connected components are noise)

    пороговая насыщенность для обнаружения букв (низкая насыщенность)
    найти большие связанные компоненты (маленькие связанные компоненты - это шум)

    """
    connectivity = 4        # связь(?)
    ret, thresh_s = cv2.threshold(image_saturation, 42, 255, cv2.THRESH_BINARY_INV)  # 50 too high, 25 too low  пороговая сигментация изображения т.е. в результате получаю белые буквы на чёрном фоне
    output = cv2.connectedComponentsWithStats(thresh_s, connectivity, cv2.CV_32S)   # поиска связанных компонентов возвращает кортеж номеров компонентов и изображение с метками для компонентов статистику о каждом компоненте и их центроидах.
                                                                                    # т.е. вычисление всех компонентов, соединенных черным, и удаление тех, которые меньше нескольких пикселей
    blob_image = output[1]  # здесь находиться изображение с метками для компонентов (??)
    stats = output[2]   # здесь находиться статистика о каждом компоненте и их центроидах (??)
    
    # print('output[0]')
    # print(output[0])

    # print('output[1]')
    # for x in output[1]:
    #     print(x)

    # print('output[2]')
    # for x in output[2]:
    #     print(x)


    pop_thresh = 170
    big_blob_colour_map = make_random_colour_map_with_stats(stats, pop_thresh)  # возвращает маску случайного цвета используя статистику для большого региона(??)
    all_blob_colour_map = make_random_colour_map_with_stats(stats)  # возвращает маску случайного цвета используя статистику для всех регионов(?????)
    big_blob_coloured_image = big_blob_colour_map[blob_image]                       # output
    all_blob_coloured_image = all_blob_colour_map[blob_image]                       # output
    # display_and_output_image("big_blob_coloured_image", big_blob_coloured_image)    # display   
    # display_and_output_image("all_blob_coloured_image", all_blob_coloured_image)    # display
    letter_mask = coloured_image_to_edge_mark(big_blob_coloured_image)
    return letter_mask

def rgb_to_hsv(im):
    return cv2.cvtColor(im, cv2.COLOR_BGR2HSV)	#  для преобразования изображения из цветового RGB в HSV

def display_and_output_image(name, structure_ArrImg):
    cv2.imshow(name,structure_ArrImg)		# отображаю изображения в окне. name - имя окна, structure_ArrImg - растркартинки. Окно автоматически подгоняется под размер изображения
    file_name = os.path.join( "C:\\Users\\david\\Desktop\\", name + ".jpg")
    cv2.imwrite(file_name,structure_ArrImg)	# сохранения изображения на любом устройстве хранения. Сохранит изображение в соответствии с указанным форматом в текущем рабочем каталоге.



def main():
	structure_ArrImg = cv2.imread('image.jpg')
	print (structure_ArrImg.shape)	# возвращает структуру, форму (т.е. кол-во столбцов, строк и каналов), массива
	# display_and_output_image('window_1',structure_ArrImg)        # display
	hsv = rgb_to_hsv(structure_ArrImg)	# для преобразования изображения из цветового RGB в HSV
	image_saturation = hsv[:,:,1]  # устанавливаю яркость всей картинки в 1  # output
	# display_and_output_image("image_saturation",image_saturation)	# отображаю изображения в окне. name - имя окна, structure_ArrImg - растркартинки        # display
	letter_mask = create_letter_mask(image_saturation)
	cv2.waitKey(0)









if __name__ == '__main__':
	main()