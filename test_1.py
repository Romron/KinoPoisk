from bs4 import BeautifulSoup
import re 
import os
import os.path
import FuncParsKinopoisk_0_0_3  as FPK


# with open('pages/pageBigPoster.html',"r",encoding='utf-8') as fh:
# 	html = fh.read()

# print(FPK.pars_LinkBigPoster(html))


path_FileDateAllFilms = 'json/result_DateAboutAllFilms  TEST .json'
n_Film = 9999999


# записываю в файл result_DateAboutAllFilms .json новое значение count_FilmDownloadedPosters
with open(path_FileDateAllFilms, 'r+', encoding = 'utf-8') as file_handle:
				
	# для продолжаения работы программы с места остановки
	str_ = '  "count_FilmDownloadedPosters" : "' + str(n_Film) +'" },'
	if len(str_) < 50:
		n = 51 - len(str_)
	else:
		print('count_FilmDownloadedPosters слишком большой')
	str_ = '  "count_FilmDownloadedPosters" : "' + str(n_Film) +'"' + ' '*n + '},'

	# для продолжаения работы программы с места остановки
	file_handle.seek(63,0) 
	file_handle.write(str_)	
