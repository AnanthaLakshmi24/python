# cook your dish here
def smallest_number_of_notes(N):
    denominations = [100, 50, 10, 5, 2, 1]
    count = 0
    for note in denominations:
        count += N // note  
        N = N % note        
    return count
T = int(input())
for _ in range(T):
    N = int(input())
    print(smallest_number_of_notes(N))