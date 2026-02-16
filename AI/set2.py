# 1) Take a string input and print it

text = input("Enter a string: ")
print("You entered:", text)


# 2) Find the length of a string

text = input("Enter a string: ")
length = len(text)

print("Length of string:", length)



# 3) Print each character of a string on a new line

text = input("Enter a string: ")

for ch in text:
    print(ch)



# 4) Count characters without using len()

text = input("Enter a string: ")

count = 0
for ch in text:
    count += 1

print("Total characters:", count)




# 5) Convert a string to uppercase

text = input("Enter a string: ")
print("Uppercase:", text.upper())



# 6) Convert a string to lowercase

text = input("Enter a string: ")
print("Lowercase:", text.lower())


# 7) Check whether a string is empty or not

text = input("Enter a string: ")

if text == "":
    print("String is empty")
else:
    print("String is not empty")


# 8) Count the number of vowels in a string

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch in vowels:
        count += 1

print("Vowel count:", count)



# 9) Count the number of consonants in a string

text = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for ch in text:
    if ch.isalpha() and ch not in vowels:
        count += 1

print("Consonant count:", count)



# 10) Check whether a string contains only digits

text = input("Enter a string: ")

if text.isdigit():
    print("Only digits")
else:
    print("Not only digits")



# 11) Check whether a string starts with a vowel

text = input("Enter a string: ")

if text[0] in "aeiouAEIOU":
    print("Starts with vowel")
else:
    print("Does not start with vowel")


# 12) Check whether a string ends with a consonant

text = input("Enter a string: ")

last = text[-1]

if last.isalpha() and last not in "aeiouAEIOU":
    print("Ends with consonant")
else:
    print("Does not end with consonant")



# 13) Count how many times a character appears

text = input("Enter a string: ")
char = input("Enter character to count: ")

count = 0

for ch in text:
    if ch == char:
        count += 1

print("Occurrences:", count)



# 14) Reverse a string using a loop

text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reversed string:", reverse)


# 15) Check whether a string is a palindrome

text = input("Enter a string: ")

if text == text[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")



# 16) Count the number of words in a string

text = input("Enter a sentence: ")

words = text.split()

print("Word count:", len(words))



# 17) Find the first repeated character

text = input("Enter a string: ")

seen = []

for ch in text:
    if ch in seen:
        print("First repeated character:", ch)
        break
    seen.append(ch)


# 18) Remove all spaces from a string

text = input("Enter a string: ")

result = text.replace(" ", "")

print("Without spaces:", result)



# 19) Replace all vowels with *

text = input("Enter a string: ")

result = ""

for ch in text:
    if ch in "aeiouAEIOU":
        result += "*"
    else:
        result += ch

print("Result:", result)



# 20) Sort characters of a string alphabetically

text = input("Enter a string: ")

sorted_text = sorted(text)

print("Sorted string:", "".join(sorted_text))
