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

def save_Result(dict_,path,count_LinksToFilm):

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
	#======================  до запись в существующий НЕпустой файл  =============
	if os.path.isfile(path_ToFile) :	
		size_File = os.path.getsize(path)
		if size_File != 0:
			with open(path_ToFile, 'r+', encoding = 'utf-8') as file_handle:
				
				# для продолжаения работы программы с места остановки
				str_ = '{ "count_LinksToFilm" : "' + str(count_LinksToFilm) +'"},'
				if len(str_) < 50:
					n = 50 - len(str_)
				else:
					print('count_LinksToFilm слишком большой')
					return False
				str_ = '{ "count_LinksToFilm" : "' + str(count_LinksToFilm) +'"' + ' '*n + '},\n'

				# для продолжаения работы программы с места остановки
				file_handle.seek(2,0) 
				file_handle.write(str_)	

				file_handle.seek(size_File-3,0) 
				file_handle.write(',\n')		
				json.dump(dict_, file_handle, indent = 2, ensure_ascii = False)
				file_handle.write('\n]')		
				return 
	# ===================  запись в новый или пустой файл  ========================

	# для продолжаения работы программы с места остановки
	str_ = '{ "count_LinksToFilm" : "' + str(count_LinksToFilm) +'"},'
	if len(str_) < 50:
		n = 50 - len(str_)
	else:
		print('count_LinksToFilm слишком большой')
		return False
	str_ = '{ "count_LinksToFilm" : "' + str(count_LinksToFilm) +'"' + ' '*n + '},\n'


	with open(path_ToFile, 'w', encoding = 'utf-8') as file_handle:
		file_handle.write('[\n')

		# для продолжаения работы программы с места остановки
		file_handle.seek(2,0) 
		file_handle.write(str_)	

		json.dump(dict_, file_handle, indent = 2, ensure_ascii = False)
		file_handle.write('\n]')

# ================================================================================================================
# ================================================================================================================

path = 'E:\\Projects\\Parsers_2020\\Prosto_film\\kinopoisk\\For_tests\\test_1.json'
dict_ = {
	'Id_kinopisk':'1345615',
	'Title':'История Beastie Boys',
	'ProductionYear':'2020',
	'Genre':['документальный',' биография',' музыка'],
	'Actors':['Адам Хоровиц','Майк Даймонд','Beastie Boys']
	}

dict_2 = {
	'Id_kinopisk':'+++++++++++++++++++++++++++++++++++++++++++',
	'Title':'99999999999999',
	'ProductionYear':'2020',
	'Genre':['документальный',' биография',' музыка'],
	'Actors':['111111111111','2222222222222222','33333333333333']
	}

count_LinksToFilm = 500

save_Result(dict_2,path,11238)
size_File = os.path.getsize(path)
with open(path, 'r+', encoding = 'utf-8') as file_handle:
# 	str_ = '{ "count_LinksToFilm" : "' + str(count_LinksToFilm) +'"},'
# 	if len(str_) < 50:
# 		print(len(str_))
# 		n = 50 - len(str_)
# 		print('n = ', n)

# 	str_ = '{ "count_LinksToFilm" : "' + str(count_LinksToFilm) +'"' + ' '*n + '},'

# 	print(len(str_))

# 	file_handle.seek(2,0) 
# 	file_handle.write(str_)	
# 	# # list_from_file = file_handle.read()
# 	file_handle.seek(0) 
	list_from_file = json.load(file_handle)
	print(list_from_file)