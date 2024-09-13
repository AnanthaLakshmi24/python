tel=eval(input('enter marks of tel'))
hin=eval(input('enter marks of hin' ))
mat=eval(input('enter marks of mat'))
soc=eval(input('enter marks of soc'))
sum=(tel+hin+mat+soc)
avg=sum/2
print(f"{avg:0.3f}")
percent=(sum/400)*100
print(f"{percent:0.3f}" + "%")