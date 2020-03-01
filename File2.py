import requests
import xlwt
from bs4 import BeautifulSoup

class check:
    def returnLink(url):    
        html = html = requests.get(url,'html.parser').text;
        bs = BeautifulSoup(html)
        possible_links = bs.findAll('a')



html = requests.get('https://obo.genaud.net/backmatter/indexes/sutta/sutta_toc.htm?fbclid=IwAR1qUeiUyochbcaE_dtpC7_5oMzd8bag8mbgOcCt_ZJWGGWLhcypt4pplxI','html.parser').text;
workbook = xlwt.Workbook(encoding="utf-8")
sheet = workbook.add_sheet('Suthra')
row =2
column = 0

bs = BeautifulSoup(html)
possible_links = bs.findAll('a')
print(possible_links)
link=possible_links[0]
if link.has_attr('href'):
    url=link['href']
    url='../../../backmatter/indexes/sutta/dn/idx_digha_nikaya.htm#p1'
    if '#p' in url:
        url = url.replace('../../..','https://obo.genaud.net')
        print(url)
        text = url.split('#')
        page = requests.get(text).text
        htmlpage = BeautifulSoup(page)
        links = bs.findAll('a')

        #print(text[0])
        #htmlpage = BeautifulSoup(page)
        #if (htmlpage.find('a',{"id":"p1"}) != 'None'):
            #print('aa')
    else:
        #print('fa')

        
    



