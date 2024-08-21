def my_function(string, substring):
    res = [i for i in range(len(string)) if string.startswith(substring, i)]
    print ("The start indices of the substrings are : " + str(res))

test_str = "GeeksforGeeks is best for Geeks"
test_sub = "Geeks"

my_function(test_str, test_sub)