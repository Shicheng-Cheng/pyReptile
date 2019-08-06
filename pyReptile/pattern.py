# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 16:09:41 2019

@author: Dell
"""
#清洗数据类
from bs4 import BeautifulSoup
import lxml
from lxml.html.soupparser import fromstring as soup_parse

class DataPattern(object):
    def cssSelector(self,response,selector,**kwargs):
        parser=kwargs.get('parser','html.parser')
        tempList=[]
        soup=BeautifulSoup(response,parser)
        temp=soup.select(selector=selector)
        for i in temp:
            tempList.append(i.getText())
        return tempList

    def xpath(self,response,selector,**kwargs):
        parser=kwargs.get('parser','html.parser')
        try:
            soup=soup_parse(response,features=parser)
        except:
            soup=lxml.html.fromstring(response)
        temp=soup.xpath(selector)
        tempList = []
        for i in temp:
            tempList.append(i.text)
        return tempList
dataPattern=DataPattern()