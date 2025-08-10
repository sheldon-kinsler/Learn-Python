import nltk  #natural language toolkit library in python. What python uses as it's human language model to train AI

sample_text = 'I am learning Generative AI'  
tokens = nltk.word_tokenize(sample_text.lower())  #convert the sameple text to lowercase and split it into tokens. Meaning split into individual separate words.
                        
print('Tokens:', tokens)    #tokens are what LLMs use to train, understand language, and generate text. They are small bits of data, like individual words

                            #The process of making raw data like text trainable for language models is known as tokenization

#Result: 'I am learning Generative AI' becomes ['i', 'am', 'learning', 'generative', 'ai']


##################################################################################################

from nltk.tokenize import word_tokenize   #from the nltk library we are importing the word.tokenize which breaks text up into smaller pieces called token 
import nltk    #brings in the full nltk library so we can use other functions like below
nltk.download('punkt')   #downloads a dataset needed for tokenizing text. Contains data that tells NLTK how to break sentences and words correctly for various languages

sample_text = 'I love programming!'
tokens = word_tokenize(sample_text)  #breaks up the text

print('Tokens:', tokens)

#Result: Tokens: ['I', 'love', 'programming', '!']


###################################################################################################

import nltk     #importing the tool kit
from nltk.tokenize import word_tokenize     #the function that breaks up the text string into tokens
from nltk.util import ngrams  #a new function we're bringing in that puts different tokens together to see how often 2 or so words go together. Creates a probability of each pair

sample_text = 'I am learning NLP(Natural Language Processing)'
tokens = word_tokenize(sample_text)  #breaks the string up

# Unigram
unigrams = list(ngrams(tokens, 1))   #breaks p one word at a time. Same as just using word_tokenize
print('Unigrams:', unigrams)

# Bigram
bigrams = list(ngrams(tokens, 2))  #pairs the words up by 2 at a time to see how often they occur togther 
print('Bigrams:', bigrams)

# Trigram
trigrams = list(ngrams(tokens, 3))   #groups words 3 at a time to see how often they appear together in this odrder
print('Trigrams:', trigrams)

#Result: 
#Unigrams: [('I',), ('am',), ('learning',), ('NLP',), ('(',), ('Natural',), ('Language',), ('Processing',), (')',)]
#Bigrams: [('I', 'am'), ('am', 'learning'), ('learning', 'NLP'), ('NLP', '('), ('(', 'Natural'), ('Natural', 'Language'), ('Language', 'Processing'), ('Processing', ')')]
#Trigrams: [('I', 'am', 'learning'), ('am', 'learning', 'NLP'), ('learning', 'NLP', '('), ('NLP', '(', 'Natural'), ('(', 'Natural', 'Language'), ('Natural', 'Language', 'Processing'), ('Language', 'Processing', ')')]
