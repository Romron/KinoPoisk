from bs4 import BeautifulSoup
import re 
import os
import os.path
import FuncParsKinopoisk_0_0_3  as FPK


with open('pages/pagePoster.html',"r",encoding='utf-8') as fh:
	html = fh.read()

FPK.pars_LinksPosters(html)