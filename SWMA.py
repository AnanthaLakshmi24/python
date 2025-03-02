# cook your dish here
t=int(input())
while(t>0):
    a,b = map(int,input().split())
    ka = int(str(a)[::-1])
    kb = int(str(b)[::-1])
    
    if ka > b or ka > kb or a>b or a>kb:
        print("yes")
    else:
        print("no")
    t-=1