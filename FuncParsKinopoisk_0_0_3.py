from bs4 import BeautifulSoup
import requests
import array 
import requests.exceptions 
import re 


def parsDateFilms():

	






	arrResult = '	*** test ***'
	return arrResult



def requestsURLThroughProxy(url,proxyIP = 0,_timeout=2,headers={'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}	):

	# Добавить оброботку протоколов SOKS

	if proxyIP:
		http_proxy = "http://" + proxyIP
		https_proxy = "https://" + proxyIP 
		proxies = {"http": http_proxy,
				   "https":https_proxy}
	# Попытка подключения к URLу
	try:
		response = requests.get(url,headers=headers,proxies=proxies,timeout=_timeout)
		response.encoding = 'utf-8'
	# Вывод результата в случаи успеха:
		
		return response.text
	# Оброботка исключний:
	except Exception as err:
		# Вывод результата в случаи	неудачи
		# print('          proxy is not work')
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
	print('      -=  captcha  =-')
	return True


def countProxyList(counterProxyList,mounthProxyList=1):
	
	

	if counterProxyList < mounthProxyList :
		counterProxyList += 1
	else:
		counterProxyList = 1
	
	proxyList = 'proxyList_' + str(counterProxyList)
	
	print('countProxyList:  ' + proxyList)
	return proxyList






# если этот файл используеться как подключаемый модуль то выполняються объявленные ф-ции
# если этот файл используеться "сам по себе" то выполняються строки после этого услдовия
if __name__ == '__main__':		
	# print("Этот файл должен использоваться как подключаемый модуль!")

	parsLinksAllFilmsInYear()
 