from pyReptile.pattern import  dataPattern
from pyReptile.Spider import request

url = 'https://movie.douban.com/subject/3168101/comments'
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
                          'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 '\
                          'Safari/537.36' }
r=request.get(url,headers=headers)
print(r)
title=dataPattern.cssSelector(r['text'],'#content > h1')

print(title)

selector='div.comment> p > span'
comment=dataPattern.cssSelector(r['text'],selector,parser='html5lib')
print(comment)