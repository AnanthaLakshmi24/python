# cook your dish here
for _ in range(int(input())):
    n,x,y = map(int,input().split())
    string = input()
    if ('0' not in string) or ('1' not in string):
        print(0)
    else:
        print(min(x,y))