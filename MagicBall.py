import random   #library with multiple random functions like picking random numbers from a list

question = input('Question:      ')   #prompts user to input a question

random_number = random.randint(1, 9)    #random.randint(1,9) picks a random number between 1 and 9 everytime you run the program. Like rolling a dice

if random_number == 1:    #setting the if statements for each number with secific answers
    answer = 'Yes - definitely'
elif random_number == 2:
    answer = 'It is decidedly so'
elif random_number == 3:
    answer = 'Without a doubt'
elif random_number == 4:
    answer = 'Reply hazy, try again'
elif random_number == 5:
    answer = 'Ask again later'
elif random_number == 6:
    answer = 'Better not tell you now'
elif random_number == 7:
    answer = 'My sources say no'
elif random_number == 8:
    answer = 'Outlook not so good'
elif random_number == 9:
    answer = 'Very doubtful'
else:
    answer = 'Error'   #break fix for if something incorrect is entered by user

print('Magic 8 Ball:  ' + answer)     #prints the random answer as the final result after the question
