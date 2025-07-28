guess = '' #user will enter guess so it starts as blank
tries = 0  #starts the number of attempts at 0

print("Number Game!!")  #title
print('-------------')
while guess != 4 and tries < 3:  #starts while loop and checks if guess does not equal 4 and tries is less than 3. 4 is our secret number
  guess = int(input("Guess a number: "))  #as long as above statement is true, will keep asking question. Why we had to start guess at a blank slot
  tries += 1  #adds 1 to tries with every guess

if guess == 4:
    print("Congrats! You won!")  #user got it right

else:
    print("Nope")  #if out of guesses they lose
