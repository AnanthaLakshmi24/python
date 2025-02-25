# cook your dish here
for _ in range(int(input())):
    a,b,c = map(int, input().split())
    d = abs(b-c)
    if a > d:
        print("YES")
    else:
        print("NO")