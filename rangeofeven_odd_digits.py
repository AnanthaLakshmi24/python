start=int(input())
stop=int(input())
for i in range (start,stop+1):
    even_count=0
    odd_count=0
    copy=i
    while copy!=0:
        last_digit=copy %10
        if last_digit%2==0:
            even_count+=1
        else:
            odd_count+=1
        copy=copy//10

    print(i,"=","even=",even_count,"odd=",odd_count)
  