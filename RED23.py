# cook your dish here
for _ in range(int(input())):
    X = int(input())
    while X % 2 == 0 or X > 3:
        X = X // 2 if X % 2 == 0 else X - 3
    print(X)
        