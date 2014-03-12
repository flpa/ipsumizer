#! /usr/bin/python

from collections import deque
import sys


lorems = deque(open("lorem.txt").read().replace(' ', ''))

for char in sys.stdin.read():
    if char.isalpha():
        loremChar = lorems.popleft()
        lorems.append(loremChar)
        if char.isupper():
            loremChar.upper()
        else:
            loremChar.lower()
        char = loremChar

    sys.stdout.write(char)





