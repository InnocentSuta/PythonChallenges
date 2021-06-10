
#Program to check wether a year is a leap year or not. 

year = int(input("Please Enter a year : "))

#check if the year is divisible by 4 and 400 and not by 100

if year % 4 == 0 and (year % 400 == 0 or year % 100 != 0):
    
    print(year, "is a leap year ")
    
else:
    print(year, "is not a leap year ")



