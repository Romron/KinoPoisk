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

def save_Result(dict_,path='',mode=0):
	timeStart = time.strftime("%d-%m-%Y %H.%M.%S", time.localtime())

	if path:
		arr_path = re.split(r'[/\\\\]',path)
		fileName = arr_path[len(arr_path)-1]
		dirName = arr_path[len(arr_path)-2]	
		pathDir = os.path.dirname(os.path.abspath(__file__)) + dirName		
		if not os.path.exists(pathDir) :
			os.mkdir(pathDir)
		path_ToFile = path
	else:
		path_ToFile = timeStart +' .json'


	with open(path_ToFile, 'w', encoding = 'utf-8') as file_handle:
		file_handle.write('TEST-=-TEST-=-TEST-=-TEST-=-TEST-=-TEST-=-')
	# arr_path = re.split(r'[/\\\\]',path)
	# print(arr_path)
	# print(len(arr_path))
	# fileNam = arr_path[len(arr_path)-1]
	# dirNam = arr_path[len(arr_path)-1]

	# print(dirName)
	print(path_ToFile)


# ================================================================================================================
# ================================================================================================================

# path = 'F:\\Python project\\ParsProxy\\Proxylist\\proxylist 31-07-2020 18.59.49 .json'
path = 'F:/Python project/ParsProxy/Proxylist/5 .json'
dict_ = {
	'Id_kinopisk':'1345615',
	'Title':'История Beastie Boys',
	'ProductionYear':'2020',
	'Genre':['документальный',' биография',' музыка'],
	'Actors':['Адам Хоровиц','Майк Даймонд','Beastie Boys']
}
save_Result(dict_,path)
