import nltk

from nltk import word_tokenize

raptext = open(""datasets_rap/eminem.txt""), "r").read()
tokens = word_tokenize(raptext)
print(tokens)

