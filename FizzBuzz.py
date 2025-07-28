#game that helps kids with division
#1-100
#For multiples of 3, print "Fizz" instead of the number.
#For multiples of 5, print "Buzz" instead of the number.
#Here's the tricky part: For multiples of 3 and 5, print "FizzBuzz".

for i in range(1,101, 1):  #for each number in the range of 1-101 cunting up by 1
    if i % 3 == 0 and i % 5 == 0:  #the modulo operator, %, can find multiples of a number. If (num) % 3 == 0 it is a mutiple of 3 with 0 remainder
        print("FizzBuzz")          #9 % 3 == 0 as 3 goes into 9 perfectly. 10 % 3 == 1 because 3*3=9 and then 1 remainder to get to 10
    elif i % 3 == 0:
        print("Fizz")    # first if statement checks for where both coditions are true. Numbers like 15 are divisble by both 3 and 5
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)   #this gets every other number that isn't divisible by 3 or 5 to show up as the normal number
