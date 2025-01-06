t=int(input())
for i in range(t):
    n=int(input())
    if n%3==0:
        print("0")
    else:
        x=(n//3)+1
        y=x*3
        z=y-n
        print(z)