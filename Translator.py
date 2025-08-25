pip install translate #install the library for translating straight in your terminal

import translate
from translate import Translator    #the specific library we need for this

translator = Translator(to_lang='it')  #creating the translator object. 'it' is Italian, but can put any language you want, like 'es' for Spanish

text = input('What would you like to translate? ')   #phrase to be translated. Having user complete this phrase

translation = translator.translate(text)   #performing the translation using the correct library

print('Translated Text: ', translation)    #print the translated text

#output: 'Ciao, come stai?'
