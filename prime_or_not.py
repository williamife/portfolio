#5. Write a program that asks a user for a number and then tests whether it is prime or not and prints out...
# “The number is prime” or “The number is not prime”.

number = int(input("Enter a number: "))

if number > 1:
    for i in range(2,number):
        if (number % i) == 0:
            print(number, "is not a prime number")
            break
    else:
        print(number, "is a prime number")
else:
    print(number, "is not a prime number")