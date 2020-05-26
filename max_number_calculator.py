#1. Write a Python function to find the Max of three numbers, then ask the user for three numbers and test it.

def max(x , y , z):

    if (x != y and y != z):
        if x > y and x > z:
            print(x, "is the max of three numbers")
        elif y > x and y > z:
            print(y, "is greatest of three numbers")
        elif z > x and z > x:
            print(z, "is greatest of three numbers")
        #For some reason this line of code doesn't seem to execute
        elif x == y or y == z:
            print("There are equal numbers, try again")

print("Enter three number below and the Quiz Master will return the max number")
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

max(x , y , z)
