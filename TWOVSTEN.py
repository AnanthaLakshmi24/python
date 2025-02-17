# cook your dish here
for _ in range(int(input())):
    x = int(input())
    if x%5!=0:
        print(-1)
        continue
    if x%10==0:
        print(0)
    else:
        print(1)
        