# cook your dish here
for i in range(int(input())):
    k = int(input())
    for i in range(52,0,-1):
        if i % k == 0:
            print(52-i)
            break
