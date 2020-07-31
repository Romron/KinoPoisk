import os 
import FuncParsKinopoisk_0_0_3  as FPK
import re


# with open('pages/Start at  30-07-2020 10.06.57 .html', 'r', encoding='UTF-8') as file_handle:	
#     html = file_handle.read()


# dict_Result = FPK.parsDateFilms(html)


# print(dict_Result)


URL = 'https://www.kinopoisk.ru/film/1199655/'

result = re.sub(r'[(https://www\.kinopoisk\.ru/film/)/]','',URL)

print(result)