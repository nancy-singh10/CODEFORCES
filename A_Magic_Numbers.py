n=(input())
flag=True
i=0
while (i<len(n)):
    if n[i:i+3]=="144":
        i=i+3
    elif n[i:i+2]=="14":
        i=i+2
    elif n[i:i+1]=='1':
        i=i+1
    else:
        flag=False
        break
if flag==True:
    print("YES")
else:
    print("NO")
