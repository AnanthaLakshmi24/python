# cook your dish here
def arr(s):
    for i in s:
        if s.count(i)> 2:
            return 'no'
    return 'yes'
for _ in range(int(input())):
    n= int(input())
    s= list(map(int, input().split(' ')))
    print(arr(s))