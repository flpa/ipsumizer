#! /usr/bin/python

from collections import deque
import sys
import codecs

lorems = deque()
for char in open("lorem.txt").read():
    if char.isalpha():
        lorems.append(char)

for char in codecs.getreader("utf-8")(sys.stdin).read():
    if char.isalpha():
        loremChar = lorems.popleft()
        lorems.append(loremChar)
        if char.isupper():
            loremChar.upper()
        else:
            loremChar.lower()
        char = loremChar

    sys.stdout.write(char)





