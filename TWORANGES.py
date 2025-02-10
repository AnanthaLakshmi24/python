# cook your dish here
for i in range(int(input())):
    a,b,c,d=map(int,input().split())
    lst=[]
    for j in range(a,b+1):
        lst.append(j)
    for k in range(c,d+1):
        if(k not in lst):
            lst.append(k)
    print(len(lst))