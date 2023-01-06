# main function in python for printing output / later
def main():
  print(context_linker)
  print(context_linker2)


# idea of a context linker is, to link words, which makes sense in a context
def context_linker():
  #context = [letters_big, letters_small]
  link = input("Enter link to generate a word: ")
  if link == "link":
    print(link)


context_linker = context_linker()


#a function to link words into sentences
def context_linker2():
  words = [nouns, verbs, adjectives]
  link2 = input("Enter link2 to generate a syntax: ")
  if link2 == "link2":
    print(words)


context_linker2 = context_linker2()
print(context_linker2)
