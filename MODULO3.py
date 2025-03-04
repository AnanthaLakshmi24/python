# cook your dish here
T = int(input())
for i in range(T):
    A,B = map(int,input().split())
    count = 0
    while (A % 3 != 0) and (B % 3 != 0):
        dif = abs(A-B)
        if (A > B):
            A = dif
        else:
            B = dif
        count += 1
    print(count)
        
