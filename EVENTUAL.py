# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    my_set = set(s)
    flag = 1
    for i in my_set:
        if s.count(i) % 2 != 0:
            flag = 0
    if(flag):
        print("YES")
    else:
        print("NO")