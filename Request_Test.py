# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 18:50:10 2019

@author: Dell
"""
import sys
sys.path.append(r'E:/pyReptile') 
#import pyReptile
from pyReptile.Spider import request

url='http://httpbin.org/get'
params={
        'pyReptile':'spiderGet'}
cookies={
        'pyReptils':'spiderCookies'}

redis_host='127.0.0.1'
r=request.get(url,params=params,cookies=cookies,
              redis_host=redis_host)
print(r.get('text',''))
print("*"*20)
url='http://httpbin.org/post'
data={
      'pyReptile':'spiderPost'}
cookies={
    'pyReptils':'spiderCookies'}
r=request.post(url,data=data,cookies=cookies)
print(r.get('text',''))