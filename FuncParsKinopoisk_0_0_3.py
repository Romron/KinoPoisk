from bs4 import BeautifulSoup
import requests
import array 
import requests.exceptions 
import re 


def parsDateFilms(html):

	dict_Result = {
		'Id_kinopisk':'test',
		'Title':'',
		'ProductionYear':'', 
		'Country':'',
		'Genre':'',
		'Actors':[],
		'Producer':'',
		'Scenario':[],
		'Director':[],
		'WorldPremiere':'',
		'Duration':'',
		'RatingIMDb':'',
		'CashFilm':'',
		'link_PagePosters':'',
		}
	
	soup = BeautifulSoup(html, 'lxml')
	try:
		dict_Result['Title'] = soup.find('span',{ "class":"styles_title__2l0HH" }).text
		dict_Result['ProductionYear'] = soup.find('div',text="Год производства").nextSibling.contents[0].text
		dict_Result['Country'] = soup.find('div',text="Страна").nextSibling.contents[0].text
		Genre =  soup.find('div',text="Жанр").nextSibling.contents[0].text.split(',')
		for x in Genre:
			if x != '...':
				dict_Result['Genre'].append(x)
		Actors = soup.find('h3',text="В главных ролях").nextSibling.contents
		[dict_Result['Actors'].append(x.text) for x in Actors]  	# НАЗЫВАЕМОЕ списковое включение
		dict_Result['Producer'] = soup.find('div',text="Режиссер").nextSibling.contents[0].text
		Scenario = soup.find('div',text="Сценарий").nextSibling.contents
		for x in Scenario:
			if x != ', ':
				dict_Result['Scenario'].append(x.text)
		Director = soup.find('div',text="Продюсер").nextSibling.contents
		for x in Director:
			if x != ', ' :
				if x.text != '...':
					dict_Result['Director'].append(x.text)
		dict_Result['WorldPremiere'] = soup.find('div',text="Премьера в мире").nextSibling.contents[0].text
		Duration = soup.find('div',text="Время").nextSibling.contents[0].text.split(' /')
		dict_Result['Duration'] = Duration[0]
		dict_Result['RatingIMDb'] = soup.find('span', { "class":"styles_valueSection__19woS" }).text
		dict_Result['link_PagePosters'] = soup.find('a',text=re.compile('Изображения')).get('href')
		CashFilm = soup.find('div',text="Сборы в мире").nextSibling.contents[0].text
		CashFilm = re.sub(r'[\xa0]','',CashFilm).split(' = ')
		dict_Result['CashFilm'] = CashFilm[1]
	except Exception:
		print('      -= Something is apsent =-')
	return dict_Result


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
	print("Этот файл должен использоваться как подключаемый модуль!")

 