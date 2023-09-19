'''
File: 6.5.py
File Created: 2023/09/19 08:35:04
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

d = {"students": [{"name": "A", "sex": "M"}, {"name": "B", "sex": "C"}]}

for k1 in d.keys():
    for k2 in d[k1]:
        for k3 in k2.keys():
            print(k3, k2[k3])