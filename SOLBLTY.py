# cook your dish here
for _ in range(int(input())):
    x,a,b = map(int,input().split())
    temp_rise = 100-x
    sol = temp_rise*b + a
    g = 10*sol
    print(g)