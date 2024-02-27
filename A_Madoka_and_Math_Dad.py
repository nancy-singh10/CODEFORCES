n = int(input())
l = []

for i in range(n):
    l.append(int(input()))

for i in range(n):
    if l[i] % 3 == 0 or l[i] % 3 == 2:
        j = 2
        while l[i] > 0:
            print(str(j), end='')
            l[i] = l[i] - j
            j = 3 - j

    elif l[i] % 3 == 1:
        j = 1
        while l[i] > 0:
            print(str(j),end='')
            l[i] = l[i] - j
            j = 3 - j
    print()
