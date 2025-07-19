#simple calculator

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)
print(result)


#more advanced calculator

num1 = float(input("Enter a number: "))
op = input("Enter an operator: ")
num2 = float(input("Enter another number: "))


if op == "+":
   print(num1 + num2)
elif op == "-":
   print(num1 - num2)
elif op == "*":
   print(num1 * num2)
elif op == "/":
   print(num1 / num2)
else:
   print('invalid operator')
