# cook your dish here
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    if a>(b+c+d) or b>(a+c+d) or c>(a+b+d) or d>(a+b+c):
        print("YES")
    else:
        print("NO")