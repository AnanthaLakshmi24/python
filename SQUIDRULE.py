# cook your dish here
t= int(input())
s=0
for i in range(t):
    n = int(input())
    a = list(map(int, input().split())) 
    s = sum(a)
    m = min(a)
    r = s-m 
    print(r)