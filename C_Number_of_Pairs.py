n=int(input())
def solve(l,r):
    cnt=0
    for i in range (len(r)):
        for j in range(i+1,len(r)):
            if r[i]+r[j]>=l[1] and r[i] +r[j]<=l[2]:
                cnt=cnt+1
    print(cnt)
for i in range(n):
    l=list(map(int,input().split()))
    r=list(map(int,input().split()))
    solve(l,r)