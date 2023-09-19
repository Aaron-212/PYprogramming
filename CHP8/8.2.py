'''
File: 8.2.py
File Created: 2023/09/19 09:44:25
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

import requests
from lxml import etree
import chardet

url = """https://movie.douban.com/chart"""
headers = ({"User-Agent": 
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15"})

response = requests.get(url, headers=headers)

chartXPath = """//*[@id="listCont2"]"""
# //*[@id="listCont2"]/li[1]/div[2]/a
# //*[@id="listCont2"]/li[2]/div[2]/a
dom = etree.HTML(str(response.text))
for i in range(1,11):
    movies = dom.xpath(f"""//*[@id="listCont2"]/li[{i}]/div[2]/a/text()""")[0]
    movies.encode().decode("unicode-escape")
    movies = movies.replace(" ", "")
    movies = movies.replace("\n", "")
    print(f"{i}. {movies}")