import requests 
import re 
import os 
import os.path
from selenium import webdriver	# импортирую модуль вебдрайвера
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import selenium.common.exceptions
import time
import json
import keyboard
import tkinter                 #  библиотека для графических интерфейсов 



result_listProxy = []
result = []
timeout = 5		# время ожидания, в секундах, нажатия клавиши для повторного перебора result_listProxy при попаданиии страницы каптчи

pathFile = os.path.dirname(__file__)	

listProxyPagesURLs	 = [
	'http://free-proxy.cz/en/',						# по этому URLу всё работает но только 5 страниц дальше без каптчи не пускает!
	'http://www.freeproxylists.net/ru/',			    # по этому URLу всё работает но сам сайт блокируеться по IP изначально!
	'https://htmlweb.ru/analiz/proxy_list.php?perpage=20&p=', # по этому URLу всё работает
	# 'https://hidemy.name/ru/proxy-list/',
	# 'http://foxtools.ru/Proxy',		# нет ссылки "Следующая"
	# 'https://hidester.com/proxylist/',
	]

listProxyPages = [    				# для тестов
		# 'Proxy_pages/captcha_page from free-proxy.cz.html',  
		# 'Proxy_pages/freeproxylists.net.html',
		# 'Proxy_pages/free-proxy.cz.html',		
		# 'Proxy_pages/foxtools.ru.html',			
		# 'Proxy_pages/htmlweb.ru.html',			
	 	# 'Proxy_pages/foxtools.ru.txt',
	 	# 'Proxy_pages/hidester.com.txt',
		]


# result_listProxy = [				# для тестов
	# '195.154.39.255:5836', 
	# '206.127.88.18:80', 
	# ]


# test_IP_URL = 'https://2ip.ru/'		# слишком долго грузиться
# test_IP_URL = 'https://myip.ru/'




def Get_HTML(URL,mode=1,IP_proxy='',flag_return_driver=0,driver=False):
	'''
		Функция должна: 
			получать страницу по переданому URL 
		Пременяет один из указанных способов, режимов, :
			Возможные способы, режимы, получения:
				1 - Библиотека requests:	
					контроль заголовков
					передача строки юзерагента
					КУКИ
				2 - Селениум
					Очень медлено!

				3 - Библиотека Splinter
					????????????
				
				4 - Библиотека MechanicalSoup
					????????????				

				5 - Библиотека RoboBrowser
					????????????

				6 - Библиотека Mechanize
						- не выполняет Javascript на страницах, которые он просматривает (проверить)

				7 - Библиотека Scrapy
					??????????????

		Возврт значений:
			если mode=1:
				пользователь имеет возможность получить экземпляр браузера для дальнейшего использования
				 вне этой ф-ции, но тогда он отвечает за закрытие этого экземпляра браузера. 
				Есть возможность вернут в ф-цию экземпляра браузера
	'''

  	# Проверка на корректность полученных данных
	if type(URL) != str:
		print('You must input only str')
		return False

	if mode == 1:
		# print('You choso Selenium:')

		if flag_return_driver == 0 or driver == False:

			r = tkinter.Tk()		# получаем объект для доступа к параметрам экрана
			pathDriver = os.path.dirname(os.path.abspath(__file__)) + "/geckodriver.exe"
			opts = Options()
			opts.headless = False
			opts.add_argument('-width=' + str(r.winfo_screenwidth()/2))		# Устанавливаем ширину окна 
			opts.add_argument('-height=' + str(r.winfo_screenheight()))	# Устанавливаем высоту окна
			

			driver = webdriver.Firefox(executable_path=pathDriver,options=opts)	
			driver.set_window_position(r.winfo_screenwidth()/2, 0)	

			if IP_proxy:
				webdriver.DesiredCapabilities.FIREFOX['proxy'] = {
				    "httpProxy": IP_proxy,
				    "ftpProxy": IP_proxy,
				    "sslProxy": IP_proxy,
				    "proxyType": "MANUAL",
					}
		try:
			driver.get(URL)

			try:
				WebDriverWait(driver, 5).until(lambda driver: 
					driver.find_elements_by_xpath("//*[.='IP адрес']"))  
			except Exception as errMess:
				pass
				# print('Элемент не найден')
				# print(errMess)

			html = driver.page_source


		# Оброботка исключний:
		except Exception as errMess:
			print('Текущий URL недоступен')
			html = False		
		
		# Вывод результатов в зависимости от значения flag_return_driver
		if flag_return_driver and html:
			arr_result = [html,driver]
			return arr_result

		# driver.close()	# закрываю браузер
		driver.quit()	# закрываю браузер
		return html



	elif mode == 2:
		print('You choso Requests lib')
		headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
		# response = requests.get(url,headers=headers,proxies=proxies,timeout=_timeout,verify=False)
		response = requests.get(URL,headers=headers)
		response.encoding = 'utf-8'
		html = response.text

	elif mode == 3:
		
		print('You choso Splinter')
	
	elif mode == 4:
		
		print('You choso MechanicalSoup')

	elif mode == 5:
		
		print('You choso RoboBrowser')

	elif mode == 6:
		
		print('You choso Mechanize')

	elif mode == 7:
		
		print('You choso Scrapy')

def Get_ProxyIP(html):
	''' Собрать IP прокси на странице
		Вернуть список собраных IP в формате IP:port
	'''

	result_listProxy = []

	# patternProxy = r'(?:[0-9]{1,5}\.){3}[0-9]{1,3}:[0-9]{2,5}'
	pattern = r'>((?:[0-9]{1,5}\.){3}[0-9]{1,3}(?::[0-9]{2,5})?)(?:(?:</[aspan]>)?</td>\n?.*?<td.*?>([0-9]{2,5})<)?'


	result = re.findall(pattern,html)

	q = 0
	while q < len(result):
		if re.search(':', result[q][0]) == None:
			result_listProxy.append(result[q][0] + ':' + result[q][1])
		else:
			result_listProxy.append(result[q][0]) 
		q += 1	


	return result_listProxy

def Get_LinkNextPage(html,URL):
	''' Найти ссылку на следующую страницу 
		Вернуть найденную ссылку в формате URLа пригодного для использоваия в Get_HTML()
	'''
	
	# для сайта:   http://free-proxy.cz/en/ 
	patern_1 = r'"([\w\d/\?=\.]+)">Next »</a>'
	# для сайта:   http://www.freeproxylists.net/ru/
	patern_2 = r'"\.([\w\d/\?=]+)">Следующая »</a>' 
	# для сайта:   https://htmlweb.ru/analiz/proxy_list.php?perpage=20&p=
	patern_3 = r'title="в конец" [\w =";()]+> ?([0-9]+) ?</a>'	# эта ссылка естьтолько на первой странице !!
	# для сайта:   'https://hidemy.name/ru/proxy-list/'
	# patern_4,html = 
	# для сайта:   'http://foxtools.ru/Proxy'
	# patern_5,html = 
	# для сайта:   'https://hidester.com/proxylist/'
	# patern_6,html = 
	
	URL_NextPage = ''		# для тех случаев когда следующей страницы нет

	if re.search(r'free-proxy\.cz',URL):
		href_ = re.findall(patern_1,html)
		if href_:
			link_NextPage = re.sub(r'^/en','',href_[0])
			URL_NextPage = URL + link_NextPage
		else:
			URL_NextPage == FALSE
	elif re.search(r'freeproxylists\.net',URL):
		link_NextPage = re.findall(patern_2,html)
		if link_NextPage:
			URL_NextPage = URL + link_NextPage[0]
		else:
			URL_NextPage == False   # т.е. следующей страницы на этом сайте нет!

	elif re.search(r'htmlweb\.ru',URL):
		result_3 = re.findall(patern_3,html)		# ищем максимальное количество следующих страниц
		maxMounth_NextPages = result_3[0]
		return int(maxMounth_NextPages) 


	elif re.search(r'hidemy\.name',URL):
		print('hidemy.name')

	elif re.search(r'foxtools\.ru',URL):
		print('foxtools.ru')

	elif re.search(r'hidester\.com',URL):
		print('hidester.com')


	else:
		URL_NextPage == FALSE
		print('Нет шаблона для обработки этого URLa  ',URL)

	return URL_NextPage


def check_CaptchaPage(html):
	'''
		TODO: 
			добавить патерны для разных страниц блокировки
			привести в соответствие с дракон схемой


	'''
	
	patern_1 = r'complete CAPTCHA to continue'	# для сайтов:   http://free-proxy.cz/en/  и  http://www.freeproxylists.net/ru/
	
	patern_2 = r'class="g-recaptcha-bubble-arrow"'	# для сайта:   https://htmlweb.ru/analiz/proxy_list.php?perpage=20&p=	

	if re.search(patern_1,html): 
		return 'CAPTCHA'
	elif re.search(patern_2,html): 
		return 'CAPTCHA'
	else:
		print('check_CaptchaPage(): Блокировки сайта не найдено')

	return True



# ##################################################################################################################
# ##################################################################################################################


if __name__ == '__main__':		

	driver = False
	URL_NextPage = None
	numberNext_Page = 1 	# для сайта https://htmlweb.ru/analiz/proxy_list.php

	time_Start = time.strftime("%d-%m-%Y %H.%M.%S", time.localtime())
	print(time_Start)


	# for fileName in listProxyPages:
	for URL in listProxyPagesURLs:
		
		flag_page_enumeration = 1
		count_ProxyIP = 0
		IP_proxy = ''

		print(URL)
		# print(fileName)
		
		while flag_page_enumeration:			# цикл продолжается пока есть ссылка на сл. страницу
			# для тестов:
			# with open(fileName,'r',encoding="utf-8") as file_handler:
			# 	html = file_handler.read()
			# 	flag_page_enumeration = 0

			if not URL_NextPage:
				URL_NextPage = URL

			arr_result = Get_HTML(URL_NextPage,1,IP_proxy,1,driver)	# функция возвратит arr_result[html,driver]
			if type(arr_result) == bool:
				html = arr_result
			elif type(arr_result) == list:
				html = arr_result[0]
				try:			# на тот случай если Get_HTML() вернёт только arr_result[0]
					driver = arr_result[1]
				except IndexError:
					pass

			if check_CaptchaPage(html) == 'CAPTCHA' or html == False:
				try:			# если result_listProxy нет 
					if re.search('http://free-proxy.cz/en',URL_NextPage):
						raise NameError			# генерирую исключение т.к. этот сайт не пускает дальше 5 страницы без каптчи
					if len(result_listProxy) == 0:   # если result_listProxy есть, но он равен нулю
						raise NameError			# генерирую исключение
					if count_ProxyIP < len(result_listProxy):			# Перебираю result_listProxy
						IP_proxy = result_listProxy[coиunt_ProxyIP]    
						count_ProxyIP += 1
						print(str(count_ProxyIP) + '. ' + IP_proxy)
					else:
						time1 = time.time()
						time2 = time.time()
						print("\n Перебор доступного списка прокси окончен. В списке было  " + count_ProxyIP + " прокси")
						print("Для повторного перебора нажмите Enter...")
						print("Для перехода к следующему сайту нажмите ПРОБЕЛ...\n")
						while time2 - time1 < timeout:
							if keyboard.is_pressed('Enter'):
								count_ProxyIP = 1
								break
							elif keyboard.is_pressed('space'):
								count_ProxyIP = False  # т.е. count_ProxyIP в данном случае используеться как флаг по которому программа выйдет из внешнего цыкла
								break
							time2 = time.time()
					if count_ProxyIP == False:	
						break
					# здесь по идее нужно закрывать браузер
					continue # эта строка должна вернуть прогамму к обработке тогоже URLа но сдругим IP
				except NameError:
					print('Сайт заблокирован, списка прокси нет')
					html = False
					URL_NextPage = ''	# для того чтобы на следующей итерации цыкла for обрабатывался именно новый URL а не значение link_NextPage из текущей итерации
					break 				# эта строка должна закончить оброботку текущего URLа и переходить к следующему 

			if html:
				listProxy = Get_ProxyIP(html)
				print(listProxy)		# для тестов
				for IP_Port in listProxy:
					result_listProxy.append(IP_Port)
					
					# save_toFile(IP_Port)		# запись в файл. Реализовать построчную запись
				
				# ======================================   поиск ссылки на следующую страницу  ========================================================
				if re.findall(r'htmlweb\.ru',URL_NextPage):		# в этом блоке обрабатываеться сайт htmlweb\.ru
					try:
						if numberNext_Page < maxMounth_NextPages:
							numberNext_Page += 1
							URL_NextPage = URL + str(numberNext_Page)	# т.к. URL_NextPage уже содержит цыфру в конце, a URL нет
						else:
							flag_page_enumeration = 0	# эта строка прекращает обработку текущего URLа
							URL_NextPage = 0
					except NameError: 		# если  maxMounth_NextPages не существует то это первый вызов для этого сайта
						numberNext_Page += 1			# т.к. numberNext_Page изначально равен 1
						maxMounth_NextPages = Get_LinkNextPage(html,URL)
						URL_NextPage = URL_NextPage + str(numberNext_Page)	# формирую URL второй(!) страницы
				elif (re.search(r'free-proxy\.cz',URL) or re.search(r'freeproxylists\.net',URL)) : 		# в этом блоке обрабатываеться сайты http://www.freeproxylists.net/ru/ и http://free-proxy.cz/en/
					link_NextPage = Get_LinkNextPage(html,URL)	

					if link_NextPage:			
						URL_NextPage = link_NextPage
						print('\n' + URL_NextPage)
					else:
						flag_page_enumeration  = 0	# эта строка прекращает обработку текущего URLа
						URL_NextPage = 0
				else:
					flag_page_enumeration = 0	# эта строка прекращает обработку текущего URLа
					URL_NextPage = 0
			else:

				continue
	
	if driver:	
		pass
		driver.quit()	# закрываю браузер если он всё ещё открыт

	print('\n\n')
	print(result_listProxy)

#============= Записываем полученные прокси в файл: ============

pathDir = os.path.dirname(os.path.abspath(__file__)) +  "/Proxylist"		
if not os.path.exists(pathDir) :
	os.mkdir(pathDir)

timePars = time.strftime("%d-%m-%Y %H.%M.%S", time.localtime())
fileName = pathDir + '/proxylist '+ timePars +' .json'
with open(fileName, 'w', encoding = 'utf-8') as f:
	json.dump(result_listProxy, f, indent = 2, ensure_ascii = False)	# json.dump() сама пишит в файл

time_Finish = time.strftime("%d-%m-%Y %H.%M.%S", time.localtime())
print(time_Finish)