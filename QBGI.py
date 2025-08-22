# cook your dish here
def solve():
    n=int(input())
    s=input()
    
    countB=0
    countG=0
    allowed=0
    for i in range(n):
        if s[i]=='B':
            countB += 1
        elif s[i]=='G':
            countG +=1
        allowed +=1
        if countB>2*countG:
            break
    print(allowed)
t=int(input())
for _ in range(t):
    solve()