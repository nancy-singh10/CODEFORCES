n=int(input())
l=list(map(int,input().split()))
for i in range(n):
    if l[i]>0:
        l[i]=1
    elif l[i]<0:
        l[i]=2
    else:
        l[i]=0
for i in range (n):
    print(l[i],end=" ")
