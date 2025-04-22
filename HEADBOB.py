# cook your dish here
t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    if 'Y' not in s and 'I' not in s:
        print("NOT SURE")
    elif 'I' not in s:
        print("NOT INDIAN")
    else:
        print("INDIAN")