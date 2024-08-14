def Recursive(k):
    if (k == 0 or k == 1):
        return 1
    return Recursive(k -1) * k

i = int(input('Please enter number: '))
print(Recursive(i))




