# A leap year is a year that consists of 366, and not 365, days. It roughly occurs every four years.
# More specifically, a year is considered leap if it is either divisible by 4 but not by 100 or divisible by 400.
# Write a program that asks the user for a year and replies with either: leap year or not a leap year.

year = int(input('Provide a year: ')) 

# Make use of nested if statements

if (year % 4) == 0:                 # Check if the year is divisible by 4
   if (year % 100) == 0:            # Check if the year is divisible by 100       
       if (year % 400) == 0:        # Check if the year is divisible by 400
           print('leap year')
       else:
           print('not a leap year')
   else:
       print('leap year')
else:
   print('not a leap year')