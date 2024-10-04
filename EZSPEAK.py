# cook your dish here
t=int(input())
for j in range(t):
    x=int(input())
    w=input()
    li=list(w)
    c=0
    is_easy=True
    for i in range(len(li)):
        if li[i] not in 'aeiou':
            c=c+1
            if c>=4:
                is_easy= False
                break
        else:
            c=0
    if is_easy:
        print("Yes")
    else:
        print("No")
