# loading in modules
import nltk
from nltk.tokenize import word_tokenize

# defining the text in order to tokenize
text = "What about a raptext"

# tokenize and print the pre-defined text
tokens = word_tokenize(text)
print(tokens)
