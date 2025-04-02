# cook your dish here
for i in range(int(input())):
    x,y=map(int,input().split())
    l=[]
    for j in range(x):
        h,w,p=list(map(int,input().split()))
        a=h*w
        if(p<=y):
            l.append(a)
    if(len(l)>0):
        print(max(l))
    else:
        print('no tablet')