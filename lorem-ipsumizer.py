from collections import deque

dek = deque(open("lorem.txt").read().split())
print dek.popleft()
