# cook your dish here
for t in range(int(input())):
    a = list(map(int,input().split()))
    b= a[0]-a[1]
    if b>=a[2]+a[3]+a[4]:
        print("yes")
    else: print("no")