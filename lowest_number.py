n=int(input())
l=list(map(int,input().split()))
ls=100000
for i in range (n):
    ls=min(ls,l[i])
print(ls)
