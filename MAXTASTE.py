# cook your dish here
t=int(input())
for _ in range(t):
    a, b, c, d = map(int, input().split())
    
    max_tastiness = max(a, b) + max(c, d)
    
    print(max_tastiness)
