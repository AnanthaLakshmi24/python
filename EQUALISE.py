# cook your dish here
t=int(input())
for i in range(t):
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a  # Ensure a is the smaller number
    while a < b:
        a *= 2
    print('YES' if a == b else 'NO')