# cook your dish here
def rem(x, y, a):
    t = a[:]
    t.remove(x)
    t.remove(y)
    return t[-1] - t[0]
    
for _ in range(int(input())):
    input()
    a = list(map(int, input().split()))
    a.sort()
    m = a[-1]
    n = a[0]
    tmp_a = a[:-1]
    c = tmp_a[-1]
    tmp_a = a[1:]
    d = tmp_a[0]
    val = min( rem(m, c, a), rem(m, n, a), rem(n, d, a))
    print(val)

