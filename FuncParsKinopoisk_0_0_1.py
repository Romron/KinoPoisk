from bs4 import BeautifulSoup
import requests
from array import *

from requests.exceptions import *

# import re 


def requestsURLThroughProxy(url,proxyIP,_timeout=5,headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}):

	# Добавить оброботку протоколов SOKS

	# print("    requestsURLtoProxy: yuor url and proxyIP received")

	http_proxy = "http://" + proxyIP
	https_proxy = "https://" + proxyIP 
	proxies = {"http": http_proxy,
			   "https":https_proxy}
	# Попытка подключения к URLу
	try:
		# response = requests.get(url,headers=headers,proxies=proxies,verify=False)
		response = requests.get(url,headers=headers,proxies=proxies,timeout=_timeout)
		response.encoding = 'utf-8'
	# Вывод результата в случаи успеха:
		print('requestsURLThroughProxy worked OK')
		return response
	# Оброботка исключний:
	except TimeoutError:
		# print("    TimeoutError")
		pass
	except ConnectionError as err:
		# print("    ConnectionError")
		# print('    Текст ошибки:  ' + str(err))
		pass
	except Exception as err:
		# print("    Неизвестная ошибка соединения" )
		pass
	# Вывод результата в случаи	неудачи
	print('   requestsURLThroughProxy worked FALSE')
	return False


def parsAllFilms(page):
	# def parsKinopoiskAllFilms():
	
	# тех задание:
		# найти на странице и вернуть массив ссылок на страницы фильмов

	arrResultLinks = []

	# Контроль результатов:
	print("    FuncParsKinopoisk: yuor page in the pipeline")
	print("\n\n")
	html = open('page.html',encoding='utf-8').read()

	# soup = BeautifulSoup(page, 'lxml')
	soup = BeautifulSoup(html, 'lxml')

	#	получить ID_kinopoisk 
	a_kinopoiskS = soup.findAll('a', class_='selection-film-item-meta__link')

	for a in a_kinopoiskS:
		ID_kinopoisk = a.get('href')
		# print(ID_kinopoisk)
		#	сформировать ссылку на страницу фильма
		LinkToPageFilm = 'https://www.kinopoisk.ru' + ID_kinopoisk
		# print(LinkToPageFilm)

		arrResultLinks.append(LinkToPageFilm) 

	# # контроль результатов
	# for x in arrResultLinks:
	# 	print(x)
	
	return arrResultLinks

	#   перейти на страницу фильма
	#   парсить данные
	#   сформировать итоговый массив данных



def parsFilm(page):
	
	# тех задание
		# найти на странице и сохранить в файл в json - формате: 
			# 	ID КиноПоиск
			#	Название фильма
			# 	Год производства
			# 	Страна
			# 	Жанр
			# 	Слоган
			# 	Режиссер
			# 	Сценарий
			# 	Продюсер
			# 	Оператор
			# 	Композитор
			# 	Художник
			# 	Монтаж
			# 	Премьера в мире
			# 	Возраст
			# 	Продолжительность
		# Предварительная структура массива:
			# arrResultParsKinopoisk = [
			# 		{	'ID_kinopoisk':ID_kinopoisk
			# 			'title':title,
			# 			'Production_year':Production_year,
			# 			'Country':Country,
			# 			'Genre':Ganr,
			# 			'Slogan':Slogan,
			# 			'Director':Director,
			# 			'Scenario':Scenario,
			# 			'Producer':Producer,
			# 			'Operator':Operator,
			# 			'Composer':Composer,
			# 			'Artist':Artist,		# Художник	
			# 			'Mounting':Mounting,
			# 			'Premiere': Premiere,
			# 			'AgeRatingSystem':AgeRatingSystem,		# Возрастные ограничения
			# 			'RatingIMDb':RatingIMDb,
			# 			'MovieDuration':MovieDuration,		# Продолжительность фильма
			# 			'Actors' : Actors,
			# 			}
			# 	]
	
	print(" \n\n   parsKinopoiskFilmPage: \n\n ")

	pass









	print("\n\n")
	# arrResultParsKinopoisk = arrResultParsKinopoisk.append(x)
	return arrResultFilm








# если этот файл используеться как подключаемый модуль то выполняються объявленные ф-ции
# если этот файл используеться "сам по себе" то выполняються строки после этого услдовия
if __name__ == '__main__':		
	# print("Этот файл должен использоваться как подключаемый модуль!")


	parsAllFilms()