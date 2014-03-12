from collections import deque

dek = deque(open("lorem.txt").read().split(None))
print dek.popleft()
