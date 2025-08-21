# cook your dish here
import math
n,x,y= map(int, input().split())
c_p_v = y//x
v_n = math.ceil(n/ c_p_v)
print(v_n)
