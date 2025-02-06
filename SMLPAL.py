# cook your dish here
for i in range(int(input())):
    x,y = map(int,input().split())
    half = '1'*(x//2)+'2'*(y//2)
    full = half+half[::-1]
    print(full)