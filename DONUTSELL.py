# cook your dish here
t=int(input())
for _ in range(t):
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    count = 0
    for i in range(n):
        for j in range(m):
            
            if b[j] == i+1 :
                if a[i] > 0 :
                    a[i] -= 1
                    continue
            
                elif a[i] == 0:
                    count += 1
                    continue
                    
                else:
                    break
                
                
    print(count)