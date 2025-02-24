# cook your dish here
for i in range(int(input())):
        n=int(input())
        k=list(map(int,input().split()))
        l=1
        for i in range(n-1):
                if k[i]!=k[i+1]:
                        l+=1
        print(l)