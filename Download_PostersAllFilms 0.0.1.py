
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
dir_DownloadPosters = 'posters ' + time_Start
if not os.path.exists(dir_DownloadPosters) :
	os.mkdir(dir_DownloadPosters)

with open('Proxylist/proxylist 07-08-2020 09.37.27 .json') as file_handle:	# получаю прокси из файла в список
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
	# формирую url_PagePoster = 'https://www.kinopoisk.ru' + [link_PagePosters]

	for proxyIP in list_Proxy:
		if flagCaptcha_DownloadPostersPoster != 1:
			print('    ' + str(count_proxyIP) + '. ' + str(proxyIP))
			count_proxyIP += 1
			html = FPK.requestsURLThroughProxy(url_PagePoster,proxyIP,_timeout=5)
			if html:
				print('\n\n\n***************************************\n\n\n',html,'\n\n\n***************************************\n\n\n')
				if FPK.pageCapcha(html):
					continue 
				list_LinksPosters = FPK.pars_LinksPosters(html)
				if list_LinksPosters == False:
					print('      ',url_PagePoster,'    постеров нет')
					break
			else:
				continue	# перехожу на следующий прокси в списке
		for link_Poster in list_LinksPosters:
			path_DownloadPostersPoster = dir_DownloadPosters + '_' + dict_DateAllFilm['Id_kinopisk'] + '_' + n_Poster
			respons_Poster = FPK.requestsURLThroughProxy(url_PagePoster,proxyIP,_timeout=5,mod=1)	
			
			# что вернёться если КАПТЧА????
			print(respons_Poster)

			# закрыто до выяснения "что вернёться если КАПТЧА????"
			# if respons_Poster:
			# 	if FPK.pageCapcha(respons_Poster):
			# 		flag_Captcha = 1
			#		continue   # перейти к новому proxy не теряя текущего состояния !!!
				# with open(path_DownloadPostersPoster, "wb") as code_Poster:
				#     code_Poster.write(respons_Poster.content)
				# flagCaptcha_DownloadPostersPoster = 0
			n_Poster += 1

		if flagCaptcha_DownloadPostersPoster == 1:
				continue	# переход на следующий прокси в списке
		else:
			n_Poster = 0
			count_proxyIP = 1
			break	# выхожу из перебора списка прокси т.к. список ссылок на постера закончен

# print(list_DateAllFilms[1]['Id_kinopisk'],list_DateAllFilms[1]['link_PagePosters'])


# рабочий вариант:



