# cook your dish here
n=int(input())
for i in range(n,n+3):
    if i%3==0:
        p=i
        break
for j in range(n-2,n+1):
    if j%3==0:
        q=j
        break
if (p-n)>(n-q):
    print(q)
else:
    print(p)
