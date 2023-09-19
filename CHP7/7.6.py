'''
File: 7.6.py
File Created: 2023/09/19 08:51:23
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

import random

score = [random.randint(0, 100) for i in range(10)]

f = open("./scores.temp.txt", "w")
f.write("Scores: ")
for i in score:
    f.write(str(i) + " ")
f.write(f"\nAverage: {sum(score) / len(score):.2f}")
f.close()