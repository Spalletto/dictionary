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
    else: 
        correction_words = get_close_matches(word, data.keys(), cutoff=0.75)
        if len(correction_words) > 0:
            action = input("Did you mean {alt_word} instead? [y or n]: ".format(alt_word=get_close_matches(word, data.keys(), cutoff=0.75)[0]))
            if action == 'y':
                return get_definition(correction_words[0])
            elif action == 'n':
                return ("There is no such a word in the dictionary.")
            else:
                return ("I don't understand you, sorry")
        else:
            return ("There is no such a word, try something else")
    
def main():
    user_word = input("Enter a word: ")
    output = get_definition(user_word)

    if type(output) == list:
        for item in output:
            print('-', item)
    else:
        print(output)

if __name__ == "__main__":
    main()