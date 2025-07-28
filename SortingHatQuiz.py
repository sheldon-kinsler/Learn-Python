Gryffindor = 0  #setting all houses equal to 0 at first
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
print("Do you like Dawn or Dusk?\n1)Dawn\n2)Dusk")  #1st question. \n gets a new line
answer = int(input("Enter 1-2: "))  #prompts user to input 1 or 2
if answer == 1:
    Gryffindor = Gryffindor + 1  #if the user inputs 1, add 1 point to both Gryffindor and Ravenclaw. So instead of 0 they will have 1 point each
    Ravenclaw = Ravenclaw + 1
elif answer == 2:
    Hufflepuff = Hufflepuff + 1   #if the user inputs 2, add 1 point to both Hufflepuff and Slytherin
    Slytherin = Slytherin + 1
else:
    print("Wrong input")  #break-fix for any other input
print("When I'm dead, I want people to remember me as:\n1)The Good\n2)The Great\n3)The Wise\n4)The Bold")  #2nd question
answer = int(input("Enter 1-4: "))
if answer == 1:
    Hufflepuff = Hufflepuff + 2  # depending on what user inputs, will add 2 points to a specific house
elif answer == 2:
    Slytherin = Slytherin + 2
elif answer == 3:
    Ravenclaw = Ravenclaw + 2
elif answer == 4:
    Gryffindor = Gryffindor + 2
else:
    print("Wrong input")
print("What kind of instrument most pleases your ear?\n1)The violin\n2)The trumpet\n3)The piano\n4)The drum")  #3rd question
answer = int(input("Enter 1-4: "))
if answer == 1:
    Slytherin = Slytherin + 4
elif answer == 2:
    Hufflepuff = Hufflepuff + 4  #the most points offered to any house
elif answer == 3:
    Ravenclaw = Ravenclaw + 4
elif answer == 4:
    Gryffindor = Gryffindor + 4
else:
    print("Wrong input")
highest_score = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)  #setting a variable that gets the highest score out of all the scores so far
print("--------------------------")  #printing a line separator just to look good
print(f"Final Scores:\nGryffindor: {Gryffindor}\nHufflepuff: {Hufflepuff}\nRavenclaw: {Ravenclaw}\nSlytherin: {Slytherin}")  #prints the final scores with a line separating each house with \n
print("--------------------------")
if Gryffindor >= Ravenclaw and Gryffindor >= Slytherin and Gryffindor >= Hufflepuff:
    print("Your house is: Gryffindor!")
elif Slytherin >= Gryffindor and Slytherin >= Ravenclaw and Slytherin >= Hufflepuff:  #these if statements print the house with the highest score
    print("Your house is: Slytherin!")
elif Ravenclaw >= Gryffindor and Ravenclaw >= Slytherin and Ravenclaw >= Hufflepuff:  #the equal is there just in case as a break-fix. But all ann statements must be true
    print("Your house is: Ravenclaw!")
else:
    print("Your house is: Hufflepuff!")
