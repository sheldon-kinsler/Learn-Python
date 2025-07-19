secret_word = "donkey"
guess = ""
guess_count = 0
guess_limit = 4
out_of_guesses = False

print("Secret Word Game!!")
print("Hint: An animal")

while guess != secret_word and not(out_of_guesses):
    if guess_count == 1:
        print("Hint: Close to horse")
    if guess_count == 3:
        print("Hint: Rhymes with wonkey")
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses. You lose.")
else:
     print("Congrats, you win!")
