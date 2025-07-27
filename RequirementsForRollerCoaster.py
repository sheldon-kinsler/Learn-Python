#creating requirements to ride a coaster. Must be at least 137 cm and have at least 10 credits

height = int(input("What is your height in cm? "))   #prompts user to enter height
credits = int(input("How many credits do you have? "))    #prompts user to enter amount of credits
if height >= 137 and credits >= 10:  
  print("Enjoy the ride!")
if height < 137 and credits >= 10:        #both must be true for all and statements
  print("You are not tall enough to ride")
if height >= 137 and credits < 10:
  print("You don't have enough credits")
if height < 137 and credits < 10:
  print("You have not met either requirement")
