
import os
import os.path
import requests
import json
import time
import FuncParsKinopoisk_0_0_3  as FPK

'''

+ получить ссылку на страницу постперов фильма
	+ открыть result_DateAboutAllFilms .json
	+ прочитать его в словарь
	+ пербирать словарь, для каждого элемента:
		+ получить значение полей: "Id_kinopisk" и "link_PagePosters"
		+ сформировать url_PagePoster = 'https://www.kinopoisk.ru' + [link_PagePosters]
		+ открыть страницу постперов фильма используя список прокси
		+ проверить каптчу
		+ спарсить ссылки постеров в словарь
		+ перебирать словарь ссылок постеров, для каждого элемента:
			сформировать path_DownloadPostersPoster = dir_DownloadPosters + '_' + [Id_kinopisk] + '_' + номер элемента списка
			проверить каптчу
			скачать постер
'''


time_Start = time.strftime("%d-%m-%Y %H.%M.%S", time.localtime())
print('Start at  ' + time_Start)


flagCaptcha_DownloadPostersPoster = 0
n_Poster = 0
n_Film = 0		# для того что бы перепрыгнуть нулевой элемент list_DateAllFilms и для вывода на печать 
count_proxyIP = 1
n_space = 4		# для более красивой выдачи результатов

path_FileDateAllFilms = 'json/result_DateAboutAllFilms .json'

dir_forIMG = os.path.dirname(os.path.abspath(__file__)) + '/IMG'		# TODO: создавать вложенные директории за один раз 
if not os.path.exists(dir_forIMG) :
	os.mkdir(dir_forIMG)
dir_DownloadPosters = dir_forIMG + '/posters ' + time_Start		# сохранять в отдельную папку
if not os.path.exists(dir_DownloadPosters) :
	os.mkdir(dir_DownloadPosters)

# получаю прокси из файла в список
with open('Proxy/Proxylist/proxylist 13-08-2020 10.22.03 .json') as file_handle:	
    list_Proxy = json.load(file_handle)
# получаю ссылку на страницу постперов фильма
with open(path_FileDateAllFilms, "r", encoding='utf-8') as file_handle:
    list_DateAllFilms = json.load(file_handle)
print('В обработке ', len(list_DateAllFilms), '  фильмов')

for dict_DateAllFilm in list_DateAllFilms:
	if n_Film == 0:		# перепрыгиваю нулевой элемент со служебной инфой
		n_Film += 1
		continue

	url_PagePoster = 'https://www.kinopoisk.ru' + dict_DateAllFilm['link_PagePosters']
	print(n_Film,'. ',url_PagePoster,sep='')
	n_Film += 1

	while count_proxyIP < len(list_Proxy):
		proxyIP = list_Proxy[count_proxyIP]
		print(' '*n_space + str(count_proxyIP) + '. ' + str(proxyIP))

		if flagCaptcha_DownloadPostersPoster == 0:
			count_proxyIP += 1
			html = FPK.requestsURLThroughProxy(url_PagePoster,proxyIP,_timeout=5)
			
			if html:
				if FPK.pageCapcha(html):
					continue 
				list_LinksPagesBigPosters = FPK.pars_LinksPagesBigPosters(html)		# получаю список ссылок на страницы спостерами большого размера
				if list_LinksPagesBigPosters == False:
					print('      ',url_PagePoster,'    постеров нет')
					break
			else:
				continue	# перехожу на следующий прокси в списке
		
		# сюда попадаю только в том случае если есть список ссылок на страницы c спостерами большого размера при этом в proxyIP рабочий(!) proxy 
		while n_Poster < len(list_LinksPagesBigPosters):
			link_PageBigPoster = list_LinksPagesBigPosters[n_Poster]
			link_PageBigPoster = 'https://www.kinopoisk.ru' + link_PageBigPoster
			# print('       ',link_PageBigPoster)

			# перехожу на страницу с постером большого размера и получаю ссылку для скачивания картинки
			html_BigPoster = FPK.requestsURLThroughProxy(link_PageBigPoster,proxyIP,_timeout=5)
			
			if html_BigPoster == False:	# на пока считаю что если запрос к картинке успешен то каптчи быть не может, но это необходимо проверять!!
				flagCaptcha_DownloadPostersPoster = 1
				print('          -= captcha Page Big postrer =-')
				break   # перейти к новому proxy не теряя текущего состояния !!! т.е. сохранить  n_Poster

			link_DownloadBigPoster = FPK.pars_LinkBigPoster(html_BigPoster)

			# формирую путь для сохранения файла постера
			path_DownloadPostersPoster = dir_DownloadPosters + '/' + dict_DateAllFilm['Id_kinopisk'] + '_' + str(n_Poster) + '.jpeg'		
			# URL для скачивания постера == link_Poster
			print('       ',link_DownloadBigPoster)
			respons_Poster = FPK.requestsURLThroughProxy(link_DownloadBigPoster,proxyIP,_timeout=5,mod=1)	

			# if respons_Poster == False or FPK.pageCapcha(respons_Poster.content):
			if respons_Poster == False: 	# на пока считаю что если запрос к картинке успешен то каптчи быть не может, но это необходимо проверять!!
				flagCaptcha_DownloadPostersPoster = 1
				print('          -= captcha download postrer =-')
				break   # перейти к новому proxy не теряя текущего состояния !!! т.е. сохранить  n_Poster
			else:
				with open(path_DownloadPostersPoster, "wb") as code_Poster:
				    code_Poster.write(respons_Poster.content)
				flagCaptcha_DownloadPostersPoster = 0
				n_Poster += 1

		

		if flagCaptcha_DownloadPostersPoster == 1:
				count_proxyIP += 1
				n_space = 8
				continue	# переход на следующий прокси в списке
		else:
			n_Poster = 0
			n_space = 4
			print('          -= all posters were downloadered =-')
			break	# выхожу из перебора списка прокси т.к. список ссылок на постера закончен 
					# необходимо перейти на следующую итерацию цыкла перебора ссылок на страницы постеров
	else:
		count_proxyIP = 1
		continue


# print(list_DateAllFilms[1]['Id_kinopisk'],list_DateAllFilms[1]['link_PagePosters'])


# рабочий вариант:



