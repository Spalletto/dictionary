import json

data = json.load(open('resourses/dictionary.json', 'r'))

def get_definition(word):
    return data[word]
    
def main():
    user_word = input("Enter a word: ")
    if user_word in data:
        print(get_definition(user_word))
    else: 
        print("There is not the word in the dictionary. Please, check it or try something else.")

if __name__ == "__main__":
    main()