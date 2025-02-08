# cook your dish here
for i in range(int(input())):
        n=int(input())
        k=list(map(int,input().split()))
        sat=[6,13,20,27]
        sun=[7,14,21,28]
        print(len(set(k+sat+sun)))