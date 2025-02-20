# cook your dish here
X, Y = map(int, input().split())
max_questions = X + (10 * Y)
if max_questions >= 100:
    print("YES")
else:
    print("NO")