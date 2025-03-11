# cook your dish here
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=list(map(int,input().split()))
    rj=[]
    for i in l:
        if i>=k:
            rj.append(i)
    cl=[]
    for j in range (len(rj)):
        s=rj[j]%k 
        cl.append(s)
    if len(cl)>0:
        print(min(cl))
    else:
        print(-1)   