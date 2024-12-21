# cook your dish here
N = int(input())
cumulative_p1 = 0  
cumulative_p2 = 0  
max_lead = 0       
winner = 0       
for _ in range(N):
    S, T = map(int, input().split())
    cumulative_p1 += S
    cumulative_p2 += T
    if cumulative_p1 > cumulative_p2:
        lead = cumulative_p1 - cumulative_p2
        if lead > max_lead:
            max_lead = lead
            winner = 1
    else:
        lead = cumulative_p2 - cumulative_p1
        if lead > max_lead:
            max_lead = lead
            winner = 2
print(winner, max_lead)