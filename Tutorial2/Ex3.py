# words = str.split("do tHuy dUong")
# new_words = ""
# for word in words:
#     new_words+=word[0].upper()+word[1:].lower()+" "
# print(new_words)

def my_function(string):
    words = str.split(string)
    new_word = ""
    for word in words:
        new_word+= word[0].upper() + word[1:].lower() + " "
    print (new_word)

b = input("Please enter string: ")
my_function(b)