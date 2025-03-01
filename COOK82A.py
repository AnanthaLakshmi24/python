# cook your dish here
for i in range(int(input())):
    d={}
    for i in range(4):
        t,g=map(str,input().split())
        d[t]=int(g)
    if d['Barcelona']>d['Eibar'] and d['Malaga']>d['RealMadrid']:
        print('Barcelona')
    else:
        print('RealMadrid')