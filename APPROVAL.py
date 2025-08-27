# cook your dish here
t = int(input())
for _ in range(t):
    r = list(map(int, input().split()))
    total = sum(r)
    r.sort() 
    coins = 0
    i = 0
    while total < 35 and i < 5:
        total += 10 - r[i]
        coins += 100
        i += 1
    print(coins)