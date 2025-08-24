# cook your dish here
for _ in range(int(input())):
    N, C = map(int, input().split())
    A = list(map(int, input().split()))
    
    set_A = set(A); min_A = min(A)
    for extra in range(101):
        C_new = C + extra
        if C_new not in set_A and C_new > min_A:
            print(extra); break