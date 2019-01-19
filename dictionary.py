import json
from difflib import get_close_matches

data = json.load(open('resourses/dictionary.json', 'r'))

def get_definition(word):
    word = word.lower()

    if word in data:
        return data[word] 
    elif word.title() in data:
        return data[word.title()] 
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys(), cutoff=0.75)) > 0:
        return ("Did you mean {alt_word} instead?".format(alt_word=get_close_matches(word, data.keys(), cutoff=0.75)[0])) 
    else: 
        return ("There is no the word in the dictionary. Please, check it or try something else.")
    
def main():
    user_word = input("Enter a word: ")
    print(get_definition(user_word))

if __name__ == "__main__":
    main()