from bs4 import BeautifulSoup
import re 
import os
import os.path
import FuncParsKinopoisk_0_0_3  as FPK


with open('pages/pagePoster_2.html',"r",encoding='utf-8') as fh:
	html = fh.read()

print(FPK.pars_LinksPosters(html))


# # https://st.kp.yandex.net/images/poster/sm_3375438.jpg
# # https://st.kp.yandex.net/im/poster/3/3/7/kinopoisk.ru-Varda-par-Agn_26_23232_3Bs-3375438.jpg

