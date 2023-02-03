import sys
from collections import deque

n = int(sys.stdin.readline().strip())
d = deque()

for i in range(n):
    a = int(sys.stdin.readline().strip())

    if a > 0:
        d.append(a)
    else:
        if d == deque():
            print(0)
        else:
            x = sorted(d)
            print(x[-1])
            d.remove(x[-1])