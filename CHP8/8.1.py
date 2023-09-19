'''
File: 8.1.py
File Created: 2023/09/19 09:01:02
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

import requests
import jieba

url = """https://gist.github.com/happyZYM/d3c9a1c9a73dbb9aefd8a8c9549b341d/raw/e728d4b8e1ca895514797187e0d8e1ef10baf32d/%25E7%25BA%25A2%25E6%25A5%25BC%25E6%25A2%25A6.txt"""

try:
    file = open("./hongloumeng.temp.txt", "r")
    words = jieba.lcut(file.read())
except IOError:
    print("Error: File does not appear to exist.")
    response = requests.get(url)
    file = open("./hongloumeng.temp.txt", "w")
    file.write(response.text)
    words = jieba.lcut(response.text)
file.close()

counts = {}

for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1
        
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print(word, count)