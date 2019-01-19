import json

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
        return ("There is no the word in the dictionary. Please, check it or try something else.")
    
def main():
    user_word = input("Enter a word: ")
    print(get_definition(user_word))

if __name__ == "__main__":
    main()