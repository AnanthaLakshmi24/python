# cook your dish here
t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    li=[x,y,z]
    p=li.sort()
    if li[2]>(li[0]+li[1]):
        print("NO")
    else:
        print("YES")