import nltk

from nltk.tokenize import word_tokenize

text =  open('rapbot/nltk_raptext/raptext.txt').read()

tokens = word_tokenize(text)
print(tokens)

# define a function with parts of tokenized speech
#def tokenized():
#    text = tokenize(text)
