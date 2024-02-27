n=int(input())
l=list(map(int,input().split()))
x=int(input())

flag=False
for i in range (n):
    if l[i]==x:
        flag=True
        break
    else:
        flag=False
if flag==True:
    print(i)
else:
    print(-1)