# -*- coding: utf-8 -*-
import requests
import xlsxwriter
import xlwt
import unicodedata
from bs4 import BeautifulSoup

class check:
    def returnHtml(self, url):    
        html = requests.get(url,'html.parser').text;
        bs = BeautifulSoup(html, 'lxml')
        return bs

    def hasNumbers(inputString):
        return any(char.isdigit() for char in inputString)


workbook = xlwt.Workbook(encoding="utf-8")
sheet = workbook.add_sheet('Sheet1')

obj = check()
bs = obj.returnHtml('https://obo.genaud.net/backmatter/indexes/sutta/sutta_toc.htm?fbclid=IwAR1qUeiUyochbcaE_dtpC7_5oMzd8bag8mbgOcCt_ZJWGGWLhcypt4pplxI')
mainheaders = bs.find_all('h4')
row =2
column = 0

for header in mainheaders :
    if (str(header.find('a',{'id':'DN'})) != "None"):        
        name = 'Dīgha Nikāya'
        sheet.write(row, column, name)
        link = 'https://obo.genaud.net/backmatter/indexes/sutta/dn/idx_digha_nikaya.htm'
        subPage = obj.returnHtml(link)
        subPageHeaders = subPage.find_all('h4')
        num = 1
        for subheader in subPageHeaders :            
            subName = subheader.text.split(',')[0].split('. ')[1]
            subNameEdit = unicodedata.normalize('NFKD', subName).encode('ascii','ignore')
            linkToSection = link + '#p' + str(num)
            num = num+1
            sheet.write(row, column+2, subNameEdit)
            sheet.write(row, column+3, linkToSection)
            row += 1

    elif (str(header.find('a',{'id':'MN'})) != "None"):
        name = 'Majjhima Nikāya'
        sheet.write(row, column, name)
        link = 'https://obo.genaud.net/backmatter/indexes/sutta/mn/idx_majjhima_nikaya_1.htm'
        subPage = obj.returnHtml(link)
        subPageHeaders = subPage.find_all('h4')
        subPageHeaders.pop(0)
        num = 1
        oldNumber = 1
        VaggaNo = 1
        oldName = ''
        for subheader in subPageHeaders :
            subName = subheader.text.split(',')[0]            
            #edited = unicodedata.normalize('NFKD', subName).encode('ascii','ignore')
            stringList = subName.split('. ')
            newNumber = int(stringList[0])

            if(len(oldName) == 0):
                sheet.write(row, column+1, stringList[1])
                VaggaNo +=1
            else:
                if(newNumber == VaggaNo and ("Vagga" in stringList[1])):
                    sheet.write(row, column+1, stringList[1])
                    VaggaNo +=1
                else:
                    sheet.write(row, column+2, stringList[1])
                    linkToSection = link + '#p' + str(newNumber)
                    sheet.write(row, column+3, linkToSection)
                    row += 1
            oldName = stringList[1]
            oldNumber = newNumber

    elif (str(header.find('a',{'id':'SN'})) != 'None'):
        name = 'Saɱyutta Nikāya'
    elif (str(header.find('a',{'id':'AN'})) != 'None'):
        name = 'Aŋguttara Nikāya'
    elif (str(header.find('a',{'id':'VP'})) != 'None'):
        name = 'Vinaya Piṭaka'
        
        #print(header.findNext('p'))
    elif (str(header.find('a',{'id':'KN'})) != 'None'):
        name = 'Kuddhaka Nikāya'
    elif (str(header.find('a',{'id':'ABHI'})) != 'None'):
        name = 'Abhidhamma Piṭaka'

workbook.save('excel.xls')




