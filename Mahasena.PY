# cook your dish here
t=int(input())
l=list(map(int,input().split()))
even=0
odd=0
for i in range(t):
    if l[i]%2==0:
        even+=1
    else:
        odd+=1
if even>odd:
    print("READY FOR BATTLE")
else:
    print("NOT READY")