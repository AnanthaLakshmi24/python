# cook your dish here
t = int(input())
for _ in range(t):
    p = int(input())
    if p <= 1:
        print(200)
        continue
    print(p*100)