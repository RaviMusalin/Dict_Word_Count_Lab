"""Count words in file."""
import sys
# sys.argv[1]

"""Function that counts the number of time each word appears"""

# Tokenize Function
"""
Return a list of words from the file at filename. 
"""
def tokenize(filename):
    data = open(filename)
    words_list=[]    
    for line in data:
        words = line.strip().lower().split(" ")
        words_list.extend(words)
    data.close()
    return (words_list)

# Count Words
def count_words(words):
    words_dict = {} 
    for word in words:
        print(word)
        word = normalize_text(word)
        words_dict[word] = words_dict.get(word,0) + 1
    return words_dict

# Print Word Count
def print_word_counts(word_dict):
    for word,count in word_dict.items():
        print(word,count)

# Normalize Text
def normalize_text(string):
    # string, -> string
    # "string -> string
    if string == "":
        return

    if string[-1] == ',' or string[-1] == '.':
        string_list = list(string)
        del string_list[-1]
        string = "".join(string_list)
        return string
    elif string[0] == '"':
        string_list = list(string)
        del string_list[0]
        string = "".join(string_list)
        return string 
## run the script
filename = sys.argv[1]
words = tokenize(filename)
words_dict = count_words(words)
print_word_counts(words_dict)
tokenize(sys.argv[1])