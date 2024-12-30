# cook your dish here
import math

def charlie_eats_slices(T, cases):
    results = []
    for A, B in cases:
        total_eaten = 0
        while A != B:
            if A > B:
                eat = math.ceil(A / 2)
                A -= eat
            else:
                eat = math.ceil(B / 2)
                B -= eat
            total_eaten += eat
        results.append(total_eaten)
    return results


T = int(input())
cases = [tuple(map(int, input().split())) for i in range(T)]

# Process and Output
results = charlie_eats_slices(T, cases)
for result in results:
    print(result)