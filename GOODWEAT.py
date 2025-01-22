# cook your dish here
t=int(input())
for _ in range(t):
    l=list(map(int,input().split()))
    s=0
    r=0
    for i in range(0,7):
        if l[i]==1:
	        s=s+1
        else:
            r=r+1
    if s>r:
        print("YES")
    else:
        print("NO")
	        
	 