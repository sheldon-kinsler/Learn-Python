#create simple receipt with set values

Name = "Jamie"
Item1 = "Milk"
Price1 = 3.50
Item2 = "Candy"
Price2 = 1.00
total = Price1 + Price2


print("Customer: " + Name)
print(f"Item: {Item1} - ${Price1:.2f}")
print(f"Item: {Item2} - ${Price2:.2f}")
print(f"Total: ${total:.2f}")


#create receipt with user input values

Name = input("Enter Your Name: ")
Item1 = input("Enter 1st Item: ")
Price1 = float(input("Enter the Price: "))
Item2 = input("Enter 2nd Item: ")
Price2 = float(input("Enter the Price: "))
total = Price1 + Price2

print("Customer: " + Name)
print(f"Item: {Item1} - ${Price1:.2f}")
print(f"Item: {Item2} - ${Price2:.2f}")
print(f"Total: ${total:.2f}")
print(f"Thank you for shopping with us, {Name}!")


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

