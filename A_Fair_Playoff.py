n = int(input())

def solve(l):
    max1 = max(l[0], l[1])
    min1 = min(l[0], l[1])
    max2 = max(l[2], l[3])
    min2 = min(l[2], l[3]
    # print(max1,min1,max2,min2)
    
    if max1 < min2:
        print("NO")
    elif  max2 < min1:
        print("NO")
    else:
        print("YES")
for i in range(n):
    l = list(map(int, input().split()))
    solve(l)
