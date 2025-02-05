# cook your dish here
for i in range (int(input())):
    n=int(input())
    l= list(map(int,input().split()))
    s=0
    count=0
    for i in range(0,n):
        s = s + l[i]
        if s==i+1:
            count=count+1
    print(count)
