import os 
import os.path 
import json
import time

import FuncParsKinopoisk_0_0_3  as FPK








timeStart = time.strftime("%d-%m-%Y %H.%M.%S", time.localtime())

print('Start at  ' + timeStart)


with open('json/arrLinksAllFilms 22-06-2020 09.11.09 .json') as file_handle:	# получаю ссылки из файла в список
    list_LinksToFilm = json.load(file_handle)

with open('Proxylist/proxylist 29-07-2020 08.54.06 .json') as file_handle:	# получаю прокси из файла в список
    list_Proxy = json.load(file_handle)

count_LinksToFilm = 1
count_proxyIP = 0

for Link_ToFilm in list_LinksToFilm:

	print(str(count_LinksToFilm) + '. ' + Link_ToFilm)
	
	while count_proxyIP < len(list_Proxy):
		proxyIP = list_Proxy[count_proxyIP]
	# for proxyIP in list_Proxy:

		print('    ' + str(count_proxyIP) + '. ' + str(proxyIP))

		html = FPK.requestsURLThroughProxy(Link_ToFilm,proxyIP,_timeout=7)

		count_proxyIP += 1
		if html:
			if FPK.pageCapcha(html):
				continue
			dict_Result = FPK.parsDateFilms(html)
			# заполняю поле 'Id_kinopisk'
			dict_Result['Id_kinopisk'] = re.sub(r'[(https://www\.kinopoisk\.ru/film/)/]','',Link_ToFilm)
			print(dict_Result)
			break
	else:		# для запуска перебора списка прокси по новому кругу
		count_proxyIP == 0
		continue
	count_LinksToFilm += 1
	if count_LinksToFilm > 10:
		break





# --------------------- Закрыл на время тестов -----------------------
	# pathDir = os.path.dirname(os.path.abspath(__file__)) +  "/json"		# для хранения файла с результатами работы этой ф-ции
	# if not os.path.exists(pathDir) :
	# 	os.mkdir(pathDir)
	# fileName = pathDir + '/arr_DateAllFilms '+ timeStart + ' .json'
	# if os.path.isfile(fileName):
	# 	writeMode = 'a'
	# 	print('Добавил строки в существующий файл\n')
	# else:
	# 	writeMode = 'w'
	# 	print('Создал файл для записи строк\n')
	# with open(fileName, writeMode, encoding = 'utf-8') as f:
	# 	json.dump(arr_DateAllFilms, f, indent = 2, ensure_ascii = False)


# Расчёт общего времини работы скрипта
# Хочу разницу времён, но пока не получается
timeFinish = time.strftime("%d-%m-%Y %H.%M.%S", time.localtime())
print('Finish at ' + timeFinish)





# Добавить автоматическое выключение комьпютера 




