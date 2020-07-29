from bs4 import BeautifulSoup
import requests
from array import *
from requests.exceptions import *

import re 


countProxy = 1		# Глобальная переменная используется в requestsURLThroughProxy()



def requestsURLThroughProxy(url,proxyList,_timeout=2,headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}):
	global countProxy

	# Добавить оброботку протоколов SOKS

	while countProxy < len(proxyList):
		proxyIP = proxyList[countProxy]
	
	# for proxyIP in proxyList:
		print('countProxy = ' + str(countProxy) + '   proxyIP = ' + str(proxyIP))
		countProxy += 1
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
			# print('requestsURLThroughProxy worked OK')
			return response.text
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
	countProxy = 0
	print('requestsURLThroughProxy: ProxyList is Over    countProxy = ' + str(countProxy))
	return False

def parsLinksAllFilmsInYear(Page):
	# отладочные строки:
	# def parsLinksAllFilmsInYear():
	
	arrLinksAllFilmsInYear = []
	
	# print("  parsLinksAllFilmsInYear: yuor page is being processed")
	
	# Проверка на страницу капчи:
	if pageCapcha(Page):
		print('pageCapcha')
		return False

	# отладочные строки:
	# html = open('page.html',encoding='utf-8').read()
	# soup = BeautifulSoup(html, 'lxml')
	# Рабочие строки:
	soup = BeautifulSoup(Page, 'lxml')

	# ---------------------  ПАРСИНГ ссылок  ----------------------
	#	получить ID_kinopoisk 
	a_kinopoiskS = soup.findAll('a', class_='selection-film-item-meta__link')

	for a in a_kinopoiskS:
		ID_kinopoisk = a.get('href')
		# print(ID_kinopoisk)
		#	сформировать ссылку на страницу фильма
		LinkToPageFilm = 'https://www.kinopoisk.ru' + ID_kinopoisk
		# print(LinkToPageFilm)

		arrLinksAllFilmsInYear.append(LinkToPageFilm) 

	# отладочные строки:
	# print("ParsLinksAllFilmsInYear: worked OK")
	for x in arrLinksAllFilmsInYear:
		print(x)
	


	# Рабочие строки:
	return arrLinksAllFilmsInYear



def pageCapcha(Page):
	
	soup = BeautifulSoup(Page, 'lxml')
	tegCapch = re.search('запросы, поступившие с вашего IP-адреса, похожи на автоматические', soup.text)
	
	if tegCapch == None:
		return False
	return True


def countProxyList(counterProxyList,mounthProxyList=1):
	
	

	if counterProxyList < mounthProxyList :
		counterProxyList += 1
	else:
		counterProxyList = 1
	
	proxyList = 'proxyList_' + str(counterProxyList)
	
	print('countProxyList:  ' + proxyList)
	return proxyList



def parsDateFilms():
	pass






# если этот файл используеться как подключаемый модуль то выполняються объявленные ф-ции
# если этот файл используеться "сам по себе" то выполняються строки после этого услдовия
if __name__ == '__main__':		
	# print("Этот файл должен использоваться как подключаемый модуль!")

	parsLinksAllFilmsInYear()
 