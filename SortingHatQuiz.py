Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0
print("Do you like Dawn or Dusk?\n1)Dawn\n2)Dusk")
answer = int(input("Enter 1-2: "))
if answer == 1:
    Gryffindor += 1
    Ravenclaw += 1
elif answer == 2:
    Hufflepuff += 1
    Slytherin += 1
else:
    print("Wrong input")
print("When I'm dead, I want people to remember me as:\n1)The Good\n2)The Great\n3)The Wise\n4)The Bold")
answer = int(input("Enter 1-4: "))
if answer == 1:
    Hufflepuff += 2
elif answer == 2:
    Slytherin += 2
elif answer == 3:
    Ravenclaw += 2
elif answer == 4:
    Gryffindor += 2
else:
    print("Wrong input")
print("What kind of instrument most pleases your ear?\n1)The violin\n2)The trumpet\n3)The piano\n4)The drum")
answer = int(input("Enter 1-4: "))
if answer == 1:
    Slytherin += 4
elif answer == 2:
    Hufflepuff += 4
elif answer == 3:
    Ravenclaw += 4
elif answer == 4:
    Gryffindor += 4
else:
    print("Wrong input")
highest_score = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)
print("--------------------------")
print(f"Final Scores:\nGryffindor: {Gryffindor}\nHufflepuff: {Hufflepuff}\nRavenclaw: {Ravenclaw}\nSlytherin: {Slytherin}")
print("--------------------------")
if Gryffindor >= Ravenclaw and Gryffindor >= Slytherin and Gryffindor >= Hufflepuff:
    print("Your house is: Gryffindor!")
elif Slytherin >= Gryffindor and Slytherin >= Ravenclaw and Slytherin >= Hufflepuff:
    print("Your house is: Slytherin!")
elif Ravenclaw >= Gryffindor and Ravenclaw >= Slytherin and Ravenclaw >= Hufflepuff:
    print("Your house is: Ravenclaw!")
else:
    print("Your house is: Hufflepuff!")

#could also do the last section this way for less typing. Does the same thing

#if Gryffindor == highest_score  # since we already calculated the hoghest_score we can just find the house that matches that score
#    print("Your house is: Gryffindor!")
#elif Slytherin == highest_score
#    print("Your house is: Slytherin!")
#elif Ravenclaw == highest_score
#    print("Your house is: GRavenclaw!")
#else:
#    print("Your house is: Hufflepuff!")
