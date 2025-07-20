#create simple receipt with set values

Name = "Jamie"      #setting variables that are constant
Item1 = "Milk"
Price1 = 3.50
Item2 = "Candy"
Price2 = 1.00
total = Price1 + Price2    #when total is called then add the prices


print("Customer: " + Name)  #prints string + Name variable
print(f"Item: {Item1} - ${Price1:.2f}")  #prints string + variable. f-string allows you to use one string with { } to embed variables
print(f"Item: {Item2} - ${Price2:.2f}") #looks alot cleaner without having to separate everything with "quotes" . Runs faster 
print(f"Total: ${total:.2f}")    #prints string + variable total which adds the prices
                                  #.2f adds two decimal points to the end. Best for money


#create receipt with user input values

Name = input("Enter Your Name: ")   #prompts user to input value for each below variable
Item1 = input("Enter 1st Item: ")
Price1 = float(input("Enter the Price: "))
Item2 = input("Enter 2nd Item: ")
Price2 = float(input("Enter the Price: "))
total = Price1 + Price2   #when total is called then add the user input prices

print("Customer: " + Name)  #prints string + user entered value for Name variable
print(f"Item: {Item1} - ${Price1:.2f}")
print(f"Item: {Item2} - ${Price2:.2f}")
print(f"Total: ${total:.2f}")
print(f"Thank you for shopping with us, {Name}!") #without the fstring would have to say:
                                                  #print("Thank you for shopping with us, " + Name + "!")
                                                  #much cleaner this way
#improvements to above code

Name = input("Enter Your Name: ")
Item1 = input("Enter 1st Item: ")
Item1 = Item1.capitalize()  #capitalizes first letter of word and keeps the rest lowercase
Price1 = float(input("Enter the Price: "))
Item2 = input("Enter 2nd Item: ")
Item2 = Item2.capitalize()   #capitalizes first letter of word and keeps the rest lowercase. If they enter "mIlK" it will show up as "Milk"
Price2 = float(input("Enter the Price: "))
total = Price1 + Price2

print("Customer: " + Name)
print(f"Item: {Item1} - ${Price1:.2f}")
print(f"Item: {Item2} - ${Price2:.2f}")
print(f"Total: ${total:.2f}")
print(f"Thank you for shopping with us, {Name}!")

