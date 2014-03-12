from collections import deque

dek = deque(open("lorem.txt").read().split(' '), 10)
print dek.pop()
