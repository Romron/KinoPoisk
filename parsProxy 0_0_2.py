import requests
from requests.exceptions import *
from urllib3.exceptions import *
from bs4 import BeautifulSoup
import re 


# страничная пагинация, но порты отдельно:
	# https://hidemy.name/ru/proxy-list/
	# http://free-proxy.cz/ru/
	# http://foxtools.ru/Proxy?page=1
	# http://www.freeproxylists.net/ru/?c=&pt=&pr=&a%5B%5D=1&a%5B%5D=2&u=0



# paternProxy = r'(?:\d{1,3}\.){3}\d{1,3}:\d{2,5}'  проверяно рабочий!!!


paternProxy = r'<td.*(?:\d{1,3}\.){3}\d{1,3}'  сделать шаблон НЕ жадным
paternPopr  = r':\d{2,5}'

with open("1.html",'r',encoding="utf-8") as file_handler:
	page = file_handler.read()
	# print(page)

proxyIP = re.findall(paternProxy,page)

for x in proxyIP:
	print(x)


