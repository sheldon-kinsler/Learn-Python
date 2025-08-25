pip install textblob   #install correct library in terminal

import textblob

from textblob import TextBlob   #call the library

text = input('Enter word or phrase to check for spelling: ')  #prompting user to enter word or phrase to spell check

blob = TextBlob(text)   #creating a textblob object with the text

corrected_text = blob.correct()  #creating the object that actually does the spell checking of the text

print(f'Original Text: {text}')  #print the original entered text

print(f'Corrected Text: {corrected_text}')   #print the corrected text after spell check


#Output: 
#Enter word or phrase to check for spelling: I am learnig so much
#Original Text: I am learnig so much
#Corrected Text: I am learning so much
