# cook your dish here
t=int(input())
for i in range (t):
    x,y,z=map(int,input().split())
    li=[x,y,z]
    s=max(li)
    li.remove(s)
    p=max(li)
    print(p)