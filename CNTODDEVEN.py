# cook your dish here
t = int(input())
for _ in range(t):
    x = int(input())
    r=[]
    e=0
    o=0
    for i in range(1,x+1,1):
        if x%i == 0:
            r.append(i)
    for j in range(len(r)):
        if r[j]%2==0:
            e=e+1
        else:
            o=o+1
    print(o,e)
        
            