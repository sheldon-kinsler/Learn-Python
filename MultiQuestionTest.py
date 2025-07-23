#In a separate file or tab in python, create an object with the question format

class Question: #creating a new class that holds the blueprints for creating objects. Like a variable that holds mold for creating object to call later
    def __init__(self, prompt, answer): #__init__(self, ) creates the outline for the attributes of the object we're creating. Think of an intake form with all of your info you're entering
        self.prompt = prompt # this sets the attributes you enter equal to this object. So python knows what info you're entering. It knows this is the prompt, not the answer
        self.answer = answer # this tells python the value you are entering is the answer and not the prompt or anything else. Like getting the inner query to match the outer query


#in main file or tab call that object to use it to create questions:


from Question import Question #bring in the object blueprints that you created in the other file. Think of it ike a join between the files

question_prompts = [    #creating a variable that contains a list of strings. These strings are 3 questions. Strings always need brackets [ ]
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",    #each string includes a question and multiple-choice options
    "What color are bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n", #\n is a line break
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

questions = [   
    Question(question_prompts[0], "a"),     #creating another variable with strings that references the above question_prompts by their index number. Begins with the Question class blueprint
    Question(question_prompts[1], "c"),     #includes the correct answer to each question
    Question(question_prompts[2], "b")      #this is like the answer key
]   #class      #prompt          #answer


def run_test(questions):   #creating a function that runs the test. Function with the required parameter inside
    score = 0    #starts the score at 0 for the user
    for question in questions:    #creating a for loop that loops through each question in the above questions list once
        answer = input(question.prompt)    #creating a variable that prompts the user to type a value. Question.prompt displays each question to the user
        if answer == question.answer:   #compares the user input to the answer key to see if they are correct or not. Boolean value
            score += 1  #if the user got the question right (if above is true) then add 1 to the score
    print(f"You got {score} / {len(questions)} Correct") #once the loop is complete (all questions have been answered) display the message with the score they have over the total number of questions

run_test(questions)  #calling the function with the questions variable to run the test
