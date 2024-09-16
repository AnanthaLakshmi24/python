stones="aAAbbbo"
jewels="aA"
c=0
for i in stones:
    for j in jewels:
        if i==j:
            c=c+1
print(c)