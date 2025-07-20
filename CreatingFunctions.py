def sayhi():  #def is to define the function
   print("Hello User")  #value that the function will print when called

sayhi()    #prints Hello User



def sayhi():     #def is to define the function
   name = input("What is your name? ")   #prompts user to enter value for the name variable
   print("Hello " + name)   #displays string "Hello" and the user entered variable, name

sayhi()   #function with input variable inside



def sayhi():
  name = input("What is your name? ")
  age = input("How old are you? ")
  print("Hello " + name + ", you are " + age + " years old.")

sayhi()    #multiple input variables inside of a function



isdog = True   #setting the variable to true

if isdog == "true":
   print("Just a baby")   #if variable, isdog, is true, then display "Just a baby"
else:
   print("not a baby")   #if variable is false, then print "not a baby"

#functions with if


isdog = input("Is a dog? ")  #prompts user to enter value for variable isdog

if isdog == "True" or isdog == "true" or isdog == "yes" or isdog == "Yes":
    print("Just a baby")  #lots of or statements that act as catchalls so user can enter multiple things and still make statement true
else:
    print("Not a baby")  # if user enters any other value this message will be displayed

