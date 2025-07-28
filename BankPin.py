print('BANK OF Sheldon')  #this is my bank

pin = int(input('Enter your PIN: '))  #prompts user to enter pin

while pin != 1234:  #setting the pin to 1234
  pin = int(input('Incorrect PIN. Enter your PIN again: '))  #if user enters any pin other than 1234 they will be prompted to enter another pin

if pin == 1234:
  print('PIN accepted!')  #they got in
