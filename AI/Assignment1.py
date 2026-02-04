# 1. Print “Hello, World!” on the screen.
print("Hello, World!")


# 2. Declare variables of different types (int, float, string) and print their values and types.
a = 10
b = 3.5
c = "Python"

print(a, type(a))
print(b, type(b))
print(c, type(c))


# 3. Take two numbers as input and perform addition, subtraction, multiplication, division, and modulus.
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)


# 4. Swap two numbers using a temporary variable and without a temporary variable.
p = int(input("Enter p: "))
q = int(input("Enter q: "))

temp = p
p = q
q = temp
print("Swapped using temp:", p, q)

p, q = q, p
print("Swapped without temp:", p, q)


# 5. Input a number and check if it is even or odd.
n = int(input("Enter a number: "))

if n % 2 == 0:
    print("Even")
else:
    print("Odd")


# 6. Find the largest number among three input numbers using if-else statements.
a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)


# 7. Implement a calculator that can perform +, -, *, / operations based on user input.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+ - * /): ")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator")


# 8. Determine whether a given year is a leap year or not.
year = int(input("Enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")


# 9. Display multiplication tables from 1 to 10 using loops.
for i in range(1, 11):
    print("Table of", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)


# 10. Compute the factorial of a number using a loop.
num = int(input("Enter number: "))
fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial:", fact)


# 11. Generate the first n terms of the Fibonacci sequence.
n = int(input("Enter number of terms: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()


# 12. Calculate the sum of the digits of a given number.
num = int(input("Enter number: "))
s = 0

while num > 0:
    s = s + num % 10
    num = num // 10

print("Sum of digits:", s)


# 13. Reverse a given number and print it.
num = int(input("Enter number: "))
rev = 0

while num > 0:
    rev = rev * 10 + num % 10
    num = num // 10

print("Reversed number:", rev)


# 14. Check if a number or string is a palindrome.
val = input("Enter value: ")

if val == val[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# 15. Check whether a given number is prime.
num = int(input("Enter number: "))
is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime")
else:
    print("Not Prime")


# 16. Create a list, append elements, remove elements, find sum, max, min, and sort the list.
lst = []

lst.append(10)
lst.append(20)
lst.append(30)

print("List:", lst)
lst.remove(20)

print("Sum:", sum(lst))
print("Max:", max(lst))
print("Min:", min(lst))

lst.sort()
print("Sorted list:", lst)

# 17. Create a tuple, access elements, and demonstrate immutability.
t = (1, 2, 3)

print("Tuple:", t)
print("First element:", t[0])

# Trying to change a tuple element (this will cause an error)
# Tuples are immutable, so their values cannot be changed
#eg given below
t[0] = 10



# 18. Create a dictionary, add and remove key-value pairs, and iterate through it.
d = {"a": 1, "b": 2}

d["c"] = 3
del d["b"]

for key, value in d.items():
    print(key, value)


# 19. Take a string input and perform operations like length, slicing, reversing, and counting vowels.
s = input("Enter string: ")

print("Length:", len(s))
print("Slicing (0 to 3):", s[0:3])
print("Reversed:", s[::-1])

vowels = 0
for ch in s:
    if ch.lower() in "aeiou":
        vowels += 1

print("Vowel count:", vowels)


# 20. Write a Python program with a function to calculate the area of a circle, rectangle, and triangle.
def area_circle(r):
    return 3.14 * r * r

def area_rectangle(l, w):
    return l * w

def area_triangle(b, h):
    return 0.5 * b * h

r = float(input("Enter radius: "))
print("Area of circle:", area_circle(r))

l = float(input("Enter length: "))
w = float(input("Enter width: "))
print("Area of rectangle:", area_rectangle(l, w))

b = float(input("Enter base: "))
h = float(input("Enter height: "))
print("Area of triangle:", area_triangle(b, h))
