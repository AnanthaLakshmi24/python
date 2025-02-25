# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    l= map(int, input().split())
    m=list(l)
    m.remove(min(m))
    print(sum(m))
    
        