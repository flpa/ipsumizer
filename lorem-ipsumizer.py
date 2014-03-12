from collections import deque

dek = deque(open("lorem.txt").read().replace(' ', ''))

for char in dek:
    print "'"+char+"'"
