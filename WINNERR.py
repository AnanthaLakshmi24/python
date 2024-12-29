# cook your dish here
T = int(input())
for _ in range(T):
    P_A, P_B, Q_A, Q_B = map(int, input().split())
    penalty_P = max(P_A, P_B)
    penalty_Q = max(Q_A, Q_B)
    if penalty_P < penalty_Q:
        print("P")
    elif penalty_Q < penalty_P:
        print("Q")
    else:
        print("TIE")