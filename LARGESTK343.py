# cook your dish here
def binary():
    t = int(input().strip())  
    for i in range(t):
        x, y = map(int, input().split())  
        if x > 1:
            c = min(y // (x - 1), y)
        else:
            c = y
        print(c)  
binary()  
