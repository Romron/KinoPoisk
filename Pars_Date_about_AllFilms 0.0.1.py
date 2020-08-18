import os 
import os.path 
import json
import time
import re

import FuncParsKinopoisk_0_0_3  as FPK



timeStart = time.strftime("%d-%m-%Y %H.%M.%S", time.localtime())
print('Start at  ' + timeStart)

path_FileSaveResult = 'json/result_DateAboutAllFilms .json'
# path_FileSaveResult = 'json/result_DateAboutAllFilms  TEST .json'

count_LinksToFilm = 1
count_proxyIP = 0

# Инициализация работы программы 
if os.path.isfile(path_FileSaveResult):
	with open(path_FileSaveResult, 'r', encoding = 'utf-8') as file_handle:
		dict_ = json.load(file_handle)
		count_LinksToFilm = int(dict_[0]['count_LinksToFilm'])+1	# что бы избежать повторов т.е. count_LinksToFilm = номеру последней оброботтаной ссылки
	

with open('json/arrLinksAllFilms 22-06-2020 09.11.09 .json') as file_handle:	# получаю ссылки из файла в список
    list_LinksToFilm = json.load(file_handle)

# with open('Proxylist/proxylist 05-08-2020 20.00.19 .json') as file_handle:	# получаю прокси из файла в список
with open('Proxy/Proxylist/proxylist 17-08-2020 10.10.53 .json') as file_handle:	# получаю прокси из файла в список
    list_Proxy = json.load(file_handle)


# for Link_ToFilm in list_LinksToFilm:
while count_LinksToFilm < len(list_LinksToFilm):
	Link_ToFilm = list_LinksToFilm[count_LinksToFilm]	# для продолжаения работы программы с места остановки
	print(str(count_LinksToFilm) + '. ' + Link_ToFilm)
	
	while count_proxyIP < len(list_Proxy):
		proxyIP = list_Proxy[count_proxyIP]

		print('    ' + str(count_proxyIP) + '. ' + str(proxyIP))

		html = FPK.requestsURLThroughProxy(Link_ToFilm,proxyIP,_timeout=5)

		count_proxyIP += 1
		if html:
			if FPK.pageCapcha(html):
				continue 
			dict_Result = FPK.parsDateFilms(html)
			# заполняю поле 'Id_kinopisk'
			dict_Result['Id_kinopisk'] = re.sub(r'[(https://www\.kinopoisk\.ru/film/)/]','',Link_ToFilm)
			FPK.save_Result(dict_Result,path_FileSaveResult,count_LinksToFilm)
			print(dict_Result)
			break
	else:		# для запуска перебора списка прокси по новому кругу
		count_proxyIP = 0 
		continue
	count_LinksToFilm += 1
	# if count_LinksToFilm > 10:
	# 	break




timeFinish = time.strftime("%d-%m-%Y %H.%M.%S", time.localtime())
print('Finish at ' + timeFinish)





# Добавить автоматическое выключение комьпютера 




