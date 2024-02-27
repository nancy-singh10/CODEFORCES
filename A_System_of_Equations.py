import math

n, m = map(float, input().split())
cnt = 0

for a in range(int(math.sqrt(n)) + 1):
    for b in range(int(math.sqrt(m)) + 1):
        if (a * a + b == n) and (a + b * b == m):
            cnt = cnt + 1

print(cnt)
