# cook your dish here
def minimum_lifetime(test_cases):
    results = []
    for case in test_cases:
        N, X, lifetimes = case
        S = sum(lifetimes)
        Y = max(0, N * X - S)
        results.append(Y)
    return results

# Input Parsing
T = int(input())
test_cases = []
for _ in range(T):
    N, X = map(int, input().split())
    lifetimes = list(map(int, input().split()))
    test_cases.append((N, X, lifetimes))

# Solve and Output
results = minimum_lifetime(test_cases)
print("\n".join(map(str, results)))