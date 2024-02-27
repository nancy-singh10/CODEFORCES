n=int(input())
l=list(map(int,input().split()))
dic={}
cnt=0
for i in l:
    if i in dic:
        dic[i]=dic[i]+1
    else:
        dic[i]=1
x=min(dic.keys())
if dic[x]%2==1:
    print("Lucky")
else:
    print("Unlucky")

