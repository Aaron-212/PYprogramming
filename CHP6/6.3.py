'''
File: 6.3.py
File Created: 2023/09/19 08:31:18
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

scores = [78, 65, 45, 89, 90 ,85, 88]

# Remove highest and lowest scores
scores.remove(max(scores))
scores.remove(min(scores))

print(sum(scores) / len(scores))