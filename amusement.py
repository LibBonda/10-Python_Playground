weight = float(input('What is your weight in kg? '))
height = float(input('What is your height in centimeters? '))

if weight < 45 and height < 130:
  print("You can take a ride!")

else:
  print("Sorry, you cannot take a ride!")
  
def can_ride_carousel(height, weight):
# """Checks if a child meets the height or weight requirement to ride the carousel.
# Args:
#       height (float): Child's height in centimeters.
#       weight (float): Child's weight in kilograms.

#   Returns:
#       str: Message indicating whether the child can ride or not.
# """
    if height < 130 or weight < 45:
        return "You can take a ride!"
    else:
        return "Sorry, you cannot take a ride."

# Get user input for height and weight
height = float(input("Enter child's height in centimeters: "))
weight = float(input("Enter child's weight in kilograms: "))

# Check eligibility and print result
result = can_ride_carousel(height, weight)
print(result)