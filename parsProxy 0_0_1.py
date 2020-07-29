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

arr_IP = []

# Список доноров прокси:
proxyDonorsList = [
	'http://www.httptunnel.ge/ProxyListForFree.aspx',		# нЕВсегда работает
	'https://xseo.in/freeproxy',			
	'https://htmlweb.ru/analiz/proxy_list.php',
	'https://2ip.ru/proxy/'					
	]

paternProxy = r'(?:\d{1,3}\.){3}\d{1,3}:\d{2,5}'
# test_text = '<td colspan="1"><font class="cls1">115.124.64.234:8080</font></td>'


for URLproxyDonor in proxyDonorsList:
	
	print(URLproxyDonor + ':')
	try:
		response = requests.get(URLproxyDonor)
		response.encoding = 'utf-8'

# proxyIP = re.search(paternProxy,test_text)
		proxyIP = re.findall(paternProxy,response.text)
		for x in proxyIP:
			print('  ' + x)
		# arr_IP.append(proxyIP)

	except Exception as err:
		print('Ошибка соединение с ' + URLproxyDonor)


# for x in arr_IP:
# 	print(x)