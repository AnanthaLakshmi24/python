# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    un=a-(b+c)
    if un>=d:
        print(0)
    else:
        if un+max(b,c)>=d:
            print(1)
        else:
            print(2)
       