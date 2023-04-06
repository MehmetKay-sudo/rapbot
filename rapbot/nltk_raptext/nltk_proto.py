import nltk
from nltk.tokenize import word_tokenize

text = "Ayo, my pen and paper cause a chain reaction, to get your brain relaxin', the zany actin' maniac in action, a brainiac, in fact, son, you mainly lack attraction"

tokens = word_tokenize(text)
print(tokens)
