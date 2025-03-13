# cook your dish here
for i in range(int(input())):
    n=int(input())
    l=[]
    for j in range(n):
        l.append(int(input()))
    for j in l:
        if l.count(j)%2==1:
            print(j)
            break