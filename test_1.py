import os 
import os.path 
import json
import time
import FuncParsKinopoisk_0_0_3  as FPK
import re



# with open('pages/Start at  30-07-2020 10.06.57 .html', 'r', encoding='UTF-8') as file_handle:	
#     html = file_handle.read()


# dict_Result = FPK.parsDateFilms(html)

# print(dict_Result)

def save_Result(date,path='',mode=0):
	'''
		запись  и ДОзапись полученых данных в файл в формате json
		path обязательно должен содержать имя файла
	'''

	if path:
		arr_path = re.split(r'[/\\\\]',path)
		fileName = arr_path[len(arr_path)-1]	# TODO: добавить проверку на наличие имени файла в пути
		dirName = arr_path[len(arr_path)-2]	
		pathDir = os.path.dirname(os.path.abspath(__file__)) + dirName		
		if not os.path.exists(pathDir) :
			os.mkdir(pathDir)
		path_ToFile = path
	else:
		print('Нет пути к файлу для сохранения')
		return False

	# ЗАПИСЬ даннных в файл
	if os.path.isfile(path_ToFile):		# до запись в существующий файл
		with open(path_ToFile, 'a', encoding = 'utf-8') as file_handle:
			# file_handle.write(date)
			json.dump(date, file_handle, indent = 2, ensure_ascii = False)
	else:		# запись в новый файл
		with open(path_ToFile, 'w', encoding = 'utf-8') as file_handle:
			# file_handle.write(date)
			json.dump(date, file_handle, indent = 2, ensure_ascii = False)


# ================================================================================================================
# ================================================================================================================

# path = 'F:\\Python project\\ParsProxy\\Proxylist\\proxylist 31-07-2020 18.59.49 .json'
path = 'F:/Python project/ParsProxy/Proxylist/test_3 .json'
dict_ = {
	'Id_kinopisk':'1345615',
	'Title':'История Beastie Boys',
	'ProductionYear':'2020',
	'Genre':['документальный',' биография',' музыка'],
	'Actors':['Адам Хоровиц','Майк Даймонд','Beastie Boys']
}
# save_Result(dict_,path)

with open(path, 'r', encoding = 'utf-8') as file_handle:
	d = read(file_handle)
	data = json.load(file_handle)


	print(data)
	# data["values"] += list(a_dict)