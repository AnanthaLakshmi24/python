# cook your dish here
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    time_after=2*(180 + n)
    total_left= a + b
    print(time_after-total_left)