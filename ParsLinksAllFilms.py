import os 
import os.path 
import json
import time

from proxylist import *
from FuncParsKinopoisk_0_0_2 import *


#  переменные которые мог бы задавать пользователь:
amountYears = 20 		# количество лет для поиска, начиная с 2020
searchDepth = 20		# глубина  поиска в том же году


# переменные необходимые для работы программыи
counterYears = 0
arrAllFilmsInYear = []
arrLinksAllFilms = []


pathDir = os.path.dirname(os.path.abspath(__file__)) +  "/json"		# для хранения файла с результатами работы этой ф-ции
if not os.path.exists(pathDir) :
	os.mkdir(pathDir)
time = time.strftime("%d-%m-%Y %H.%M.%S", time.localtime())
fileName = pathDir + '/arrLinksAllFilms '+ time +' .json'



# counterProxyList = 1
# mounthProxyList = 3
# proxyList = proxyList_0

# URLPageFilmsInYear = "https://www.kinopoisk.ru/lists/navigator/2020-2020/?sort=popularity&quick_filters=foreign%2Cfilms&tab=all"
#                       https://www.kinopoisk.ru/lists/navigator/2020-2020/?page=2&sort=year&tab=all
#                       https://www.kinopoisk.ru/lists/navigator/2020-2020/?page=2&quick_filters=foreign%2Cfilms&tab=all

print('Start at ' + time)
while counterYears < amountYears:
	
	URLPageFilmsInYear = "https://www.kinopoisk.ru/lists/navigator/" + str(2020-counterYears) + "-" + str(2020-counterYears) + "/?sort=popularity&quick_filters=foreign%2Cfilms&tab=all"
	PageAllFilmsInYear = requestsURLThroughProxy(URLPageFilmsInYear,proxyList)
	
	print(URLPageFilmsInYear)

	if not PageAllFilmsInYear :
		# proxyList = countProxyList(counterProxyList)
		# print('proxyList = ' + proxyList)
		countProxy = 0
		continue
	
	if PageAllFilmsInYear:
		arrAllFilmsInYear = parsLinksAllFilmsInYear(PageAllFilmsInYear)
		if not arrAllFilmsInYear:
			continue
		# ---------------------  Реализуем глубину поиска фильмов того же года  -------------
		counterDepth = 2
		while counterDepth < searchDepth:
			print('  ParsLinksAllFilms:  год  ' + str(2020-counterYears)  + '    обработано страниц:  ' + str(counterDepth-1))
			URLNextPageFilmsInYear = "https://www.kinopoisk.ru/lists/navigator/" + str(2020-counterYears) + "-" + str(2020-counterYears) + "/?page=" + str(counterDepth) + "&sort=popularity&quick_filters=foreign%2Cfilms&tab=all"
			NextPageFilmsInYear = requestsURLThroughProxy(URLNextPageFilmsInYear,proxyList)
			


			# # ------------- ОТЛАДКА  ------------
			# print('\n\n')
			# print(URLNextPageFilmsInYear)

			# print(NextPageFilmsInYear)

			# print('\n\n')




			if not NextPageFilmsInYear:			
				# proxyList = countProxyList(counterProxyList)
				countProxy = 0
				continue
			
			arrNextFilmsInYear = parsLinksAllFilmsInYear(NextPageFilmsInYear)
			if not arrNextFilmsInYear:
				continue
			
			for x in arrNextFilmsInYear:
				arrAllFilmsInYear.append(x)
			counterDepth +=1
	
	else:
		ERROR = "ParsLinksAllFilms:   The PageAllFilmsInYear is not available"
		continue
	
	print('Обработка страниц ' + str(2020-counterYears) + ' года окончена \n' )
	

	if os.path.isfile(fileName):
		writeMode = 'a'
		print('Добавил строки в существующий файл\n')
	else:
		writeMode = 'w'
		print('Создал файл для записи строк\n')

	with open(fileName, writeMode, encoding = 'utf-8') as f:
		json.dump(arrAllFilmsInYear, f, indent = 2, ensure_ascii = False)



	arrLinksAllFilms.append(arrAllFilmsInYear)

	counterYears += 1

#  Расчёт общего времини работы скрипта
# timeFinish = time.strftime("%d-%m-%Y %H.%M.%S", time.localtime())
# print('Start at ' + time)
# print('Finish at ' + timeFinish)

# Вывод результатов
n = 0
for x in arrLinksAllFilms:
	for y in x:
		n += 1
		print(str(n)+'. ' + str(y))


# Добавить автоматическое выключение комьпютера 




