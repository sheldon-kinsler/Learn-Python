print('BANK OF Sheldon')  #this is my bank

pin = int(input('Enter your PIN: '))  #prompts user to enter pin

while pin != 1234:  #setting the pin to 1234
  pin = int(input('Incorrect PIN. Enter your PIN again: '))  #if user enters any pin other than 1234 they will be prompted to enter another pin

if pin == 1234:
  print('PIN accepted!')  #they got in



#adding protection with a limit of incorrect pins


print('BANK OF Sheldon')  #this is my bank

pin = int(input('Enter your PIN: '))  #prompts user to enter pin
limit = 2 #only giving the user a certain number of guesses before they get locked out
pin_count = 0 #starting the pin count at 0


while pin != 1234 and pin_count < limit:  # creating a while loop that will continue until they enter 1234
  pin = int(input('Incorrect PIN. Enter your PIN again: '))  #if user enters any pin other than 1234 they will be prompted to enter another pin
  pin_count += 1 #every pin guess the count goes up by 1
if pin == 1234:
    print('PIN accepted!')  #they got in
else: print('PIN rejected. Locked out!')  #if user puts in an incorrect pin too many times loop ends


