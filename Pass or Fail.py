# cook your dish here
t=int(input())
for i in range(t):
    a,b,p=map(int,input().split())
    c=b*3 
    k=a-b 
    i=-k
    s=c+i 
    if s>=p:
        print("PASS")
    else:
        print("FAIL")