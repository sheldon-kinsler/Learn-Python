#simple calculator

num1 = input("Enter a number: ")  #prompts user to enter a number for this variable(num1)
num2 = input("Enter another number: ")    #prompts user to enter a number for this variable(num2)
result = int(num1) + int(num2)    #adds the two user entered numbers together as a result
print(result)  #displays the result of the above calculation


#more advanced calculator

num1 = float(input("Enter a number: "))  #prompts user to enter a number for this variable(num1). Using float allows the user to enter a decimal
op = input("Enter an operator: ")  #prompts user to enter an operator (+-/*)
num2 = float(input("Enter another number: "))  #prompts user to enter another number for this variable(num2)


if op == "+":
   print(num1 + num2)   #if the user entered a +, adds the numbers together
elif op == "-":
   print(num1 - num2)   #if the user entered a -, asubtracts the numbers
elif op == "*":
   print(num1 * num2)   #if the user entered a *, multiplies the numbers together
elif op == "/":
   print(num1 / num2) #if the user entered a /, divides the numbers
else:
   print('invalid operator')   #if user enters any other symbol or character then it is invalid
