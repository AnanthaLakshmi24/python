# cook your dish here
for _ in range(int(input())):
    n = int(int(input()))
    a = list(map(int, input().split()))
    odd  = 0
    for i in a:
        if i%2 != 0:
            odd +=1
    if (odd%2!=0 and n>1):
        print(2)
    else:
        print(1)