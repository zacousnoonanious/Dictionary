import json
from difflib import get_close_matches
data = json.load(open("data.json"))

if __name__ == "__main__":
    print('welcome to the dictionary application! Enter a word to begin to see the definition for that word.')

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    else:
        possiblewords = get_close_matches(word, data.keys())
        return "That word doesn't exist in the data. Did you mean to enter the word {0} or {1}?".format(possiblewords[0], possiblewords[1])



word = input("Enter word: ")
print(translate(word))


