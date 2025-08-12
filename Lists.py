friends = ['tom', 'mark', 'steve', 'joe']
          # 0       1       2        3     index numbers start at 0 on left
print(friends[0])

#prints out tom 
#starts with 0 at left. -1 is far right



friends = ['tom', 'mark', 'steve', 'joe']
          # 0       1       2        3     index numbers
print(friends.index('steve'))

#tells you what index number steve is located. In this case 2


friends = ['tom', 'mark', 'steve', 'joe']
          # 0       1       2        3    index numbers
friends.append('jim')  #adds onto the end of the list
print(friends)

#output: ['tom', 'mark', 'steve', 'joe', 'jim']


friends = ['tom', 'mark', 'steve', 'joe', 'jim']
friends.pop()  #removes the last item in the list
print(friends)

#output: ['tom', 'mark', 'steve', 'joe']

friends = ['tom', 'mark', 'steve', 'joe']
friends.insert(1, 'paul')  #inserts new item into list. 1st argument is index position, 2nd is item to insert
print(friends)

#output: ['tom', 'paul', 'mark', 'steve', 'joe']

jobs = ['sales', 'IT', 'teacher']  #creating a new list
friends.extend(jobs)  #adds jobs list onto friends list
print(friends)

#output: ['tom', 'mark', 'steve', 'joe', 'sales', 'IT', 'teacher']

tuple = ('guitar', 150, 2) #creating a tuple, which is basically a list that is immutable
#if you wanted to change one of the values in the tuple, you would have to convert it to a list, make the change, and then convert back to tuple

tuple = list(tuple)  #converts tuple to a list so that you can edit value
print(tuple)
#output: ['guitar', 150, 2]

tuple(1) = 175
print(tuple)
#output: ['guitar', 175, 2]

tuple = tuple(tuple)  #converts list back into tuple so it can't be changed
print(tuple)
#output: ('guitar', 150, 2)


price = (5, 4, 3)  #creating a tuple
print(price)

#output: (5,4,3)

(bird, fish, cat) = (5, 4, 3)  #assigning variables to each value in the tuple. Have to have the same number on each side
print(f"Bird: {bird}")  
print(f"Fish: {fish}")   #this is called unpacking
print(f"Cat: {cat}")

#output: 
#Bird: 5
#Fish: 4
#Cat: 3

