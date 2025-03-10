# cook your dish here
for _ in range(int(input())):
    ball,box=map(int,input().split())

    if ball<=box and (ball!=1 and box!=1) :
        print('NO')
    else:
        if ball>=((box*(box+1))/2):
            print('YES')
        else:
            print("NO")