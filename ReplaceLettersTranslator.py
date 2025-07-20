def translate(phrase):    #defines a function called translate that requires one argument or parameter (phrase)
    translation = ""      #sets the translation to a blank string that we will build on
    for letter in phrase: #cycle through each character(letter) in the phrase
        if letter in "AEIOUaeiou":  #checks if the current letter is a vowel
            translation = translation + "g"  #if the letter is a vowel, it is replaced by a g and added to the empty translation string
        else:   #if it is not a vowel
            translation = translation + letter   #add the original letter to the translation string
    return translation  #once the loop is finished, return the entire translation string

print(translate(input("Enter a phrase: ")))  #prompts user to enter a custom phrase for the function parameter and prints that result after the translation


