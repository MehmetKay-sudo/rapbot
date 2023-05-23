import nltk

# Ensure that the NLTK data is downloaded
nltk.download('punkt')

# Function to count the number of words in a text file
def count_words(filename):
    with open(filename, 'r') as file:
        text = file.read()
        # Tokenize the text into words
        tokens = nltk.word_tokenize(text)
        # Count the number of words
        word_count = len(tokens)
    return word_count

# Specify the path to your text file
file_path = 'PATH'

# Call the function to count words in the file
word_count = count_words(file_path)

# Print the result
print("Number of words in the file:", word_count)
