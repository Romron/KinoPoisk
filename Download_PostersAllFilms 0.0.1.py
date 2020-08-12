
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

path_FileDateAllFilms = 'json/result_DateAboutAllFilms .json'

dir_forIMG = os.path.dirname(os.path.abspath(__file__)) + '/IMG'		# TODO: создавать вложенные директории за один раз 
if not os.path.exists(dir_forIMG) :
	os.mkdir(dir_forIMG)
dir_DownloadPosters = dir_forIMG + '/posters ' + time_Start		# сохранять в отдельную папку
if not os.path.exists(dir_DownloadPosters) :
	os.mkdir(dir_DownloadPosters)

# получаю прокси из файла в список
with open('Proxy/Proxylist/proxylist 12-08-2020 10.21.21 .json') as file_handle:	
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
		if flagCaptcha_DownloadPostersPoster == 0:
			print('    ' + str(count_proxyIP) + '. ' + str(proxyIP))
			count_proxyIP += 1
			html = FPK.requestsURLThroughProxy(url_PagePoster,proxyIP,_timeout=5)
			if html:
				if FPK.pageCapcha(html):
					continue 
				list_LinksPosters = FPK.pars_LinksPosters(html)
				if list_LinksPosters == False:
					print('      ',url_PagePoster,'    постеров нет')
					break
			else:
				continue	# перехожу на следующий прокси в списке
		# сюда попадаю только в том случае если есть список постеров при этом в proxyIP рабочий(!) proxy 
		for link_Poster in list_LinksPosters:
			path_DownloadPostersPoster = dir_DownloadPosters + '/' + dict_DateAllFilm['Id_kinopisk'] + '_' + str(n_Poster) + '.img'
			print('      ',path_DownloadPostersPoster)
			respons_Poster = FPK.requestsURLThroughProxy(url_PagePoster,proxyIP,_timeout=5,mod=1)	
			
			# что вернёться если КАПТЧА????

			print(respons_Poster)

			if respons_Poster.status_code != False and respons_Poster.status_code == 200:

				print('\n',respons_Poster.status_code,'\n',sep='**************')

				with open(path_DownloadPostersPoster, "wb") as code_Poster:
				    code_Poster.write(respons_Poster.content)
				flagCaptcha_DownloadPostersPoster = 0
			else:
				print('CAPTCHA')
				try:
					prin('respons_Poster.status_code   ',respons_Poster.status_code)
					prin('\n respons_Poster.text   ',respons_Poster.text,'\n')
				except Exception as err:
					pass

				# FPK.pageCapcha(respons_Poster):
				flagCaptcha_DownloadPostersPoster = 1
				continue   # перейти к новому proxy не теряя текущего состояния !!!

			n_Poster += 1

		if flagCaptcha_DownloadPostersPoster == 1:
				continue	# переход на следующий прокси в списке
		else:
			n_Poster = 0
			break	# выхожу из перебора списка прокси т.к. список ссылок на постера закончен
	else:
		count_proxyIP = 1
		continue


# print(list_DateAllFilms[1]['Id_kinopisk'],list_DateAllFilms[1]['link_PagePosters'])


# рабочий вариант:



