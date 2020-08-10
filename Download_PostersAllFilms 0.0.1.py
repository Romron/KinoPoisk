

import requests



# получить ссылку на страницу постперов фильма
	# открыть result_DateAboutAllFilms .json
	# прочитать его в словарь
	# пербирать словарь, для каждого элемента:
		# получить значение полей: "Id_kinopisk" и "link_PagePosters"
		# сформировать url_Poster = 'https://www.kinopoisk.ru' + [link_PagePosters]
		# сформировать IP_Proxy
		# открыть страницу постперов фильма
		# проверить каптчу
		# спарсить ссылки постеров в словарь
		# перебирать словарь ссылок постеров, для каждого элемента:
			# проверить каптчу
			# сформировать path_DownloadPoster = path_Download + '_' + [Id_kinopisk] + '_' + номер элемента списка
			# скачать постер



respons_Poster = requests.get(url_Poster)
with open(path_DownloadPoster, "wb") as code_Poster:
    code_Poster.write(respons_Poster.content)