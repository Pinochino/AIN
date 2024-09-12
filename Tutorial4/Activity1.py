import re;


def function(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string);

word = input('Please enter your word: ')

print(function(word)) 
