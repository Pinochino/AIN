a = int(input("The first: "))
b = int(input("The second: "))
c = int(input("The last: "))

def Triangle(a, b, c):
    if a + b >= c and a + c >= b and b + c >= a : return "This is triangle"
    return "This is not triangle"

print(Triangle(a, b, c))