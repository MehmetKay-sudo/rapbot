def main():
    print(context_linker)
    print(context_linker2)

# create two lists with letters as strings
letters_big = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
letters_small = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
nouns = ["Fast", "Fear", "Feeders", "Female", "Florida", "Fish", "Wildlife", "Conservation", "Commission", "Food", "Freshwater"]
verbs = ["apply", "ride", "create", "drive", "sing", "feel", "brake"]
adjectives = ["big", "small", "long", "short", "nice", "quite", "loud"]

# idea of a context linker is, to link words, which makes sense in a context
def context_linker():
    context = [letters_big, letters_small]
    link = input("Enter link to generate a word: ")
    if link == "link":
     print(link)

context_linker = context_linker()

#a function to link words into sentences
def context_linker2():
    words = [nouns, verbs, adjectives]
    link2 = input("Enter link2 to generate a syntax: ")
    if link2 == "link2"
    print(words)

context_linker2 = context_linker2()
print(context_linker2)

#create a bowl of letters
#letters_general = [letters_big, letters_small]

#create a bowl of words
#words = [nouns, verbs, adjectives]

#def word_set():
#    print(letters_general)
#    print(words)

#words = word_set()

#print(words)
