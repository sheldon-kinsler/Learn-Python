secret_word = "donkey"   #setting variable for what the secret word is
guess = ""    #setting the orginal guess to an empty string. This is what user will input later so it starts blank
guess_count = 0   #no guesses yet so count is at 0
guess_limit = 4   #user gets 4 guesses to guess the secret word
out_of_guesses = False  #user is not out of guesses yet. Will change this variable value later

print("Secret Word Game!!")   #displaying the title and instructions for the game
print("Hint: An animal")

while guess != secret_word and not(out_of_guesses):  #creating a while loop. While the user guess is not equal to the secret word and the user is not out of guesses, the loop will continue
    if guess_count == 1:
        print("Hint: Close to horse")  #after the user guesses 1 time, display the hint
    if guess_count == 3:   
        print("Hint: Rhymes with wonkey")   #after the user guesses 3 times, display the next hint
    if guess_count < guess_limit:  #checks to see if the current guess count(number of guesses) is less than 4(the guess limit we set earlier)
        guess = input("Enter guess: ")  # if above condition is true, than let user continue guessing
        guess_count += 1  #if above condition is true, add 1 to each guess. So after 1st guess it becomes 2nd guess
    else:
        out_of_guesses = True #if above condition (guess_count < guess_limit) is false than change the out_of_guesses variable to true
if out_of_guesses:
    print("Out of guesses. You lose.")  #once out_of_guesses is true, display the message that user lost
else:
     print("Congrats, you win!")   #if user guesses the correct word in 4 or less guesses than they win so display winning message
