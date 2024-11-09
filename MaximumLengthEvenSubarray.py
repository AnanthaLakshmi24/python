t=int(input())
for _ in range(t):
    def even_sum(n):
        return (n*(n+1))//2
        
    n=int(input())
    total=even_sum(n)
    if (total%2==0):
        print(n)
    else:
        print(n-1)