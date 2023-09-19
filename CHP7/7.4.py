'''
File: 7.4.py
File Created: 2023/09/19 08:49:17
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

colors = input("Please input yout favourite color >>>")

f = open("./colors.temp.txt", "w")
f.write(colors)
f.close()