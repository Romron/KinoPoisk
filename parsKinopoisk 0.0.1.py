 #  Чекер proxy с помощью библиотеки Requests на сайте kinopoisk.ru
 
 #  для запросов через SOCKS протоколы необходимо установить зависимости: $ pip install requests[socks]
import requests
from requests.exceptions import *
from bs4 import BeautifulSoup
import re 

from proxylist import *
from FuncParsKinopoisk_0_0_1 import *

# тех задание:
	# получаем масив проксей
	# перебираю масив проксей
	# в случаи удачи запрашиваю общую страницу фильмов данного года 
	# вызываю ф-цию parsKinopoiskAllFilms


print("test 5.py     Чекер proxy с помощью библиотеки Requests на сайте kinopoisk.ru \n")

countProxy = 0
countAnonymousProxy = 0
countTransparentProxy = 0
# headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
_timeout = 7


# url = "https://www.kinopoisk.ru/"
url = "https://www.kinopoisk.ru/lists/navigator/2020-2020/?sort=year&tab=all"
# url = "https://www.kinopoisk.ru/lists/navigator/2019-2019/?sort=year&tab=all"
# url = "https://www.kinopoisk.ru/lists/navigator/2018-2018/?sort=year&tab=all"

for proxyIP in proxyList_1:
	countProxy += 1
	
	print(str(countProxy) + ". " + proxyIP)
	
	response = requestsURLThroughProxy(url,proxyIP)	# получаю страницу с перечнем фильмов

	if response:
		print("  Proxy is OK")
		countAnonymousProxy += 1

		arrAllFilms = parsAllFilms(response.text)
		break

	else:
		print("  Proxy is do`nt work")
		continue



print('Всего проверено: '+ str(countProxy))
print('  Найденно:')
print('    рабочих:  '+ str(countAnonymousProxy) + '  или  ' + str(round(countAnonymousProxy/countProxy*100, 1)) + ' %' )










