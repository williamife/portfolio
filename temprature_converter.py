#6. Write a Python program to convert temperatures to and from celsius, fahrenheit.
#Celsius to Fahrenheit formula = ((temp/5)*9)+32 #Fahrenheit to Celsius formula = ((temp - 32)*5)/9

temperature = int(input("Enter the temperature you would like to convert: "))
scale = input("Enter C for Celsius or F for Fahrenheit: ")

if scale.upper() == "F":
    x = float((temperature * 9 / 5) + 32)
    print(x, "F")
else:
    x = float((temperature - 32) * 5 / 9)
    print(x, "C")