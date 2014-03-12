from collections import deque

dek = deque(open("lorem.txt"), 10)

print dek.pop()
