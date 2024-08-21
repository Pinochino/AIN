def process_words(input_string):
    # Split the input string by commas and remove any leading/trailing spaces
    words = [word.strip() for word in input_string.split(',')]
    
    # Remove duplicates by converting the list to a set
    unique_words = list(set(words))
    
    # Sort the list in ascending order
    unique_words.sort()
    
    # Convert the list back to a comma-separated string
    result = ', '.join(unique_words)
    
    return result

# Ask the user for input
user_input = input("Enter a list of words separated by commas: ")
result = process_words(user_input)

# Display the result
print("Output:", result)
