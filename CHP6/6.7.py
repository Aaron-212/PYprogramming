'''
File: 6.7.py
File Created: 2023/09/19 08:40:57
Author: Aaon212 (aaron212cn@outlook.com)

Copyright 2023 Aaron212
'''

freqDict = {"and": 20, "in": 10}

inStr = "Eric and Lisa are in a graden"

# Update freqDict
for word in inStr.split():
    freqDict[word] = freqDict.get(word, 0) + 1

# Print the results
print(freqDict)