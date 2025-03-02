# cook your dish here
T=int(input())
for i in range(T):
    N=int(input())
    count=0
    for j in range(N):
        S,J=list(map(int,input().split()))
        time_taken_to_judge=J-S
        if(time_taken_to_judge>5):
            count+=1 
    print(count)
    
