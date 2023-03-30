import nltk

from nltk.tokenize import word_tokenize

text = open('rapbot/nltk_raptext/eminem.txt').read()

tokens = word_tokenize(text)
print(tokens)

