# cook your dish here
from collections import Counter
for t in range(int(input())):
    n=int(input())
    a=[int(i) for i in input().split()]
    c=Counter(a)
    l=[int(i) for i in c.values()]
    m=max(l)
    print(n-m)