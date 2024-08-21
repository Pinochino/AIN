def my_function(string):
    a= {}
    for i in string:
        if i in a:
            a[i] += 1
        else:   
            a[i] = 1
    print("Count in string: ",  str(a))

b = input("Please enter string: ")
my_function(b)


