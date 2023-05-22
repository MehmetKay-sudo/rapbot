import nltk

# Ensure that the NLTK data is downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Function to count the number of words, adjectives, nouns, and verbs in a text file
def count_words_and_pos(filename):
    with open(filename, 'r') as file:
        text = file.read()
        # Tokenize the text into words
        tokens = nltk.word_tokenize(text)
        # Perform part-of-speech tagging
        pos_tags = nltk.pos_tag(tokens)
        
        # Counters for words, adjectives, nouns, and verbs
        word_count = len(tokens)
        adjective_count = 0
        noun_count = 0
        verb_count = 0

        # Iterate through the POS tags and count adjectives, nouns, and verbs
        for word, pos in pos_tags:
            if pos.startswith('JJ'):  # Adjective tags start with 'JJ'
                adjective_count += 1
            elif pos.startswith('NN'):  # Noun tags start with 'NN'
                noun_count += 1
            elif pos.startswith('VB'):  # Verb tags start with 'VB'
                verb_count += 1
    
    return word_count, adjective_count, noun_count, verb_count

# Specify the path to your text file
file_path = '/home/mehmetkaysudo/Schreibtisch/nltk/eminem.txt'

# Call the function to count words, adjectives, nouns, and verbs in the file
word_count, adjective_count, noun_count, verb_count = count_words_and_pos(file_path)

# Print the results
print("Number of words in the file:", word_count)
print("Number of adjectives in the file:", adjective_count)
print("Number of nouns in the file:", noun_count)
print("Number of verbs in the file:", verb_count)
