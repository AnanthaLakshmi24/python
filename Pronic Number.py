n=int(input())
for i in range(n):
    k=i*(i+1)
    if k==n:
        print("YES")
        break
else:
    print("NO")