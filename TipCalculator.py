total = float(input("Enter the total bill: $"))  #prompts user to enter the bill amount
percent = int(input("Enter the tip percentage: " + "%"))   #prompts user to enter desired tip percentage
tip = (total * percent)/100   #calculations for tip amount
print(f"${tip:.2f}")   #displays final tip amount with $ and 2 decimal places. .2f makes sure two decimal places
