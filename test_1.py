
import os
import cv2


def rm_watermark(path_to_poster,path_to_template):
    '''
        открыть картинку
        создать маску
            подобрать параметры
            убрать шум
        преобразования по маске
            с помощью cv2.inpaint()
    '''

    # img = cv2.imread(r"test_img/test_1.jpg")
    img = cv2.imread(path_to_poster)
    # template = cv2.imread(r"test_img/templ.jpg")
    template = cv2.imread(path_to_template)

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(gray_img, 88, 255, cv2.THRESH_BINARY_INV)
    mask = ~mask

    result = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # print("max_loc",max_loc)

    mask[0:max_loc[1],:] = 0
    mask[:,0:max_loc[0]] = 0

    poster_without_watermark = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
    
    # cv2.imshow('dst_TELEA',poster_without_watermark)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return poster_without_watermark

def main():
    list_Posters = os.listdir(path="IMG/posters")
    path_to_template = 'IMG/templ.jpg'
    dir_wiht_poster = 'IMG/posters/'
    n_Poster = 0

    # продолжение с места остановки:
        #   получить список уже изменённых файлов из папки назначения
        #   получить последний элемент этого списка
        #   получить номер этого єлемента в списке неизменённых файлов
        #   установить счётчик итераций цыкла перебора списка неизменённых файлов равным полученному номеру
    try: 
        list_PostersWithoutWoterMark = os.listdir(path="IMG/posters_without_wotermark")
        if list_PostersWithoutWoterMark:
            name_LastPosterWithoutWoterMark = list_PostersWithoutWoterMark[-1]
            namber_LastPosterWithoutWoterMark = list_Posters.index(name_LastPosterWithoutWoterMark)
            n_Poster = namber_LastPosterWithoutWoterMark
        else:
            pass            
    except:
            pass

    # for name_to_poster in list_Posters:
    while n_Poster < len(list_Posters):
        name_to_poster = list_Posters[n_Poster]
       
        paht_to_poster = dir_wiht_poster + name_to_poster
        try:
            poster_without_watermark = rm_watermark(paht_to_poster,path_to_template)
            file_Name = 'IMG/posters_without_wotermark/' + name_to_poster
            cv2.imwrite(file_Name, poster_without_watermark)
        except:
            print(name_to_poster,' is failed')

        n_Poster += 1


if __name__ == '__main__':
    main()


