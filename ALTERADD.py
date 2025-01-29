for _ in range(int(input())):
    a,b=list(map(int,input().split()))
    diff=abs(a-b)
    if (diff%3)!=2:
        print("yes")
    else:
        print("no")
    