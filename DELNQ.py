# cook your dish here
t=int(input())
for i in range(t):
    n=int(input())
    s=input()
    k=s.count("0")
    p=s.count("1")
    if k>0 and p>0:
        print(1)
    else:
        print(max(k,p))