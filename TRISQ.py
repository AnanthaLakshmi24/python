# cook your dish here
for i in range(int(input())):
    b=int(input())
    if b==1:
        print("0")
    else:
        n=(b//2)-1
        s=n*(n+1)//2
        print(s)