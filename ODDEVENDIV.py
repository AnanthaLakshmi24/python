def odd_even(x, y):
    if x == 0:
        return "No"
    if y % x == 0:
        return "Yes"
    else:
        return "No"

t= int(input())
for _ in range(t):
    x,y = map(int, input().split())
    print(odd_even(x,y))
