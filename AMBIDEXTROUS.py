# cook your dish here
for i in range(int(input())):
    l,r,m=map(int,input().split())
    if m%l==0:
        a=m//l
    elif m%l!=0:
        a=(m//l)+1
    print(a+(m//r))