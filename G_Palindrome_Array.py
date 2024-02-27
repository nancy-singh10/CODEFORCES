n=int(input())
l=list(map(int,input().split()))
i=0
j=n-1
flag=False
while(i<=j):
    if i==j:
        flag=True
    else:
        flag=False
    i=i+1
    j=j+1
if flag==True:
    print("YES")
else:
    print("NO")