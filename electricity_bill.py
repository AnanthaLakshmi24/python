unit=eval(input('enter no.of units'))
if unit<=199:
    charge=unit*1.2
elif  unit>200 and unit<400:
    charge=unit*1.50
elif unit>400 and unit<600:
     charge=unit*1.80
else:
    charge=unit*2.00

if charge<=400:
    total=charge+100
    print(total)
elif charge>400:
    total=charge+(charge*(15/100))
    print(total)