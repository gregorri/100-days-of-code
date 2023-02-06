print("Count the vowels in a string")

def count_vowels(string):
    vowels = 0
    for letter in string:
        if letter in "aeiou":
            vowels += 1
    return vowels

string = input("Enter a string: ")
lover_string = string.lower()
print(count_vowels(lover_string))
