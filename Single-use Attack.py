# cook your dish here
for _ in range(int(input())):
    H, X, Y = map(int, input().split())
    
    normal_attacks = (H - Y + X - 1) // X  #
    total_attacks = 1 + normal_attacks 
    print(total_attacks)