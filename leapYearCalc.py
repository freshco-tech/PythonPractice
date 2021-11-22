# Eample 17 leap year
year =  int(input('Enter year to findout if it is a leap year? '))

# Divisible by
if (year % 4)== 0:
    if (year % 100)== 0:
        if(year % 400)== 0:
            print(year,' is a leap year')
        else:
            print(year,' is not a leap year')
    else: print(year,' is a leap year')
else: print( year,' is not a leap year')
print('Darrius Singleton')
