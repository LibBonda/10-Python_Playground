# John earns $10 per hour for the first 160 hours in a given month. 
# For any additional hour, he earns $15 per hour. Write a program that accepts 
# an integer number of hours worked in a given month and prints John's total earnings.

hours = int(input('Provide the number of hours worked in a month: '))  # Number of hours worked in a month 

if hours <= 160:
  total_earnings = hours * 10
  print(total_earnings)
  
if hours > 160:
    total_earnings = (160 * 10) + (hours - 160) * 15
    print(total_earnings)
    
#Improved code below

hours = int(input('Provide the number of hours worked in a month: '))

# Calculate regular earnings (capped at 160 hours)
regular_earnings = min(hours, 160) * 10  # Use min() to limit hours to 160

# Calculate overtime earnings (if any)
overtime_earnings = (hours - 160) * 15 if hours > 160 else 0  # Use ternary operator for conditional calculation

# Total earnings
total_earnings = regular_earnings + overtime_earnings

print(f"John's total earnings for {hours} hours worked is: ${total_earnings:.2f}")  # Formatted output with 2 decimal places
