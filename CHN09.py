# cook your dish here
n=int(input())
for i in range(n):
    m=input()
    h=m.count("a")
    g=m.count("b")
    print(min(h,g))