# cook your dish here
t=int(input())
for _ in range(t):
    s=input()
    vowel=[s[1],s[3],s[5]]
    consonant=[s[0],s[2],s[4],s[6],s[7]]
    v=0
    c=0
    for i in vowel:
        if i in "BCDFGHJKLMNPQRSTVWXYZ":
            v=0
            break
    else:
        v=1 
    for j in consonant:
        if j in "AEIOU":
            c=0
            break 
    else:
        c=1 
    if v==0 or c==0:
        print("NO")
    elif v==1 and c==1:
        print("YES")
        