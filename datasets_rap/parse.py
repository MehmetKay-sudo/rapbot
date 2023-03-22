# import the nltk library
import nltk

# import a specific module word_tokenize
from nltk import word_tokenize

# define a variable which raptext
# open the raptext and read it
# checking two different tokens 
raptext = open("datasets_rap/eminem.txt", "r").read()
tokens = word_tokenize(raptext)
print(tokens)

raptext2 = open("datasets_rap/ceza.txt", "r").read()
tokens2 = word_tokenize(raptext)
print(tokens2)
