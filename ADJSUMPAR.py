# cook your dish here
for i in range(int(input())):
    n1=int(input())
    l1=list(map(int,input().strip().split()))[:n1]
    c=l1.count(1)
    if(c%2==0):
        print("YES")
    else:
        print("NO")