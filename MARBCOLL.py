# cook your dish here
t = int(input())
for _ in range(t):
    Nam, Man = map(int, input().split())
    App = list(map(int, input().split()))
    colle_cted = set(App)
    atype = set(range(1, Man + 1))
    not_col = atype - colle_cted
    print(len(not_col))
