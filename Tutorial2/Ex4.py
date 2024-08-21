def my_function(word):
    last_char = word[-1]
    last_two_chars = word[-2:]
    
    if last_two_chars == 'ie':
        # Rule c: Replace 'ie' with 'ying'
        print(word[:-2] + 'ying')
    elif last_two_chars == 'ee':
        # Rule d: Keep 'ee' and add 'ing'
        print(word + 'ing')
    elif last_char == 'e':
        # Rule b: Remove the 'e' and add 'ing'
        print(word[:-1] + 'ing')
    elif len(word) == 3 and word[1] in "aeiou" and word[0] not in "aeiou" and word[2] not in "aeiou":
        # Rule e: Double the final consonant and add 'ing' for consonant-vowel-consonant monosyllabic words
        print(word + word[-1] + 'ing')
    else:
        # Rule a & f: Just add 'ing'
        print(word + 'ing')

b = input("Enter the verb: ")
my_function(b)
