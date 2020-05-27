#4. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is...
# an even number. The numbers obtained should be printed in a comma-separated sequence.

even_numbers = []
for i in range(99,401):
    if i % 2 == 0:
        even_numbers.append(i)
print(even_numbers, end = " ")