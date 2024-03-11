# 1. Calculating Restaurant Bill:
# Problem: You went to a restaurant with friends and want to split the bill equally, including tip.

#Variables i)The total on the bill
         #ii)number of people to split the bill
         #iii) the tip, percentage
         
def calculate_bill():
    bill_total = float(input("Enter total amount on bill: "))       #Get bill total      
    num_people = int(input("Enter number in party: "))              #Ask user to enter bill total and number of splitters
    tip_rate = float(input("Enter Tip as a percentage: " "%"))
    
    tip_amount = round(bill_total * ((100 + tip_rate)/100) - bill_total , 3)
    cost_per_individual = round((bill_total * ((100 + tip_rate)/100))/num_people , 3)
    
    print("Overall cost: ", bill_total)
    print("tip amount: ", tip_amount)
    print("cost per person: ", cost_per_individual)
    
calculate_bill()

    
    
    #Calculate the cost to each splitter.

# factor in the tip

#calculate the cost per person

