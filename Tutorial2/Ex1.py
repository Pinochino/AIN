def my_function(a):
    lower = 0
    upper = 0

    for i in a:
        if i.isupper():  # Check if the character is uppercase
            upper += 1
        elif i.islower():  # Check if the character is lowercase
            lower += 1

    print("Uppercase characters:", upper)
    print("Lowercase characters:", lower)

b = input("Please enter a string: ")
my_function(b)
