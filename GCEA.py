# cook your dish here
for i in range(int(input())):
    n,x,y=map(int, input().split())
    a=list(map(int, input().split()))
    sum=0
    for i in range(len(a)):
        sum+=min(a[i]*x,y)
    print(sum)