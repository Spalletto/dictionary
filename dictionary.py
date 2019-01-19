import json

data = json.load(open('resourses/dictionary.json', 'r'))

def get_definition(word):
    return data[word]
    
def main():
    user_word = input("Enter a word: ")
    if user_word in data:
        print(get_definition(user_word))

if __name__ == "__main__":
    main()