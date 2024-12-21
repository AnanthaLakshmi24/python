t = int(input())
for _ in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    total_sum = sum(l)
    if total_sum % 2 != 0:
        print(-1)
        continue
    flips_needed = abs(total_sum) // 2
    count_1 = l.count(1)
    count_neg1 = l.count(-1)
    if total_sum > 0 and flips_needed <= count_1:
        print(flips_needed)
    elif total_sum < 0 and flips_needed <= count_neg1:
        print(flips_needed)
    else:
        print(0)