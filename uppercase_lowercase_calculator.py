#4. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 
# (Hint you can use isupper and islower to test for the case of the letters).

def number_case():
    sentence = str(input('Enter a sentence: ').split())
    a = {'Upper_Case':0 , 'Lower_Case':0}

    for word in sentence:
        if word.isupper():
            a['Upper_Case'] += 1
        elif word.islower():
            a['Lower_Case'] += 1

    print("There are",a['Upper_Case'],"upper case letters")
    print("There are",a['Lower_Case'],"lower case letters")

number_case()
