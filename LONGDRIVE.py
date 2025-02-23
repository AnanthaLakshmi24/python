# cook your dish here
import math
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    max_hourly_dist = 100
    diff_in_dist = (y - x) * 10
    add_hours = math.ceil(diff_in_dist / (max_hourly_dist - y))
    print(add_hours)
