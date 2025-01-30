# cook your dish here
for i in range(int(input())):
    s = input()
    
    target = 'ADVITIYA'
    step = 0
    
    for i in range(8):
        if s[i] != target[i]:
            
            if ord(s[i]) < ord(target[i]):
                step += ( ord(target[i]) - ord(s[i]) )
                
            else:
                step += ( 26 - (ord(s[i]) - ord(target[i])) )
                
    print(step)