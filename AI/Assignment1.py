print("Hello, World!")

a = 10
b = 3.5
c = "Python"
print(a, type(a))
print(b, type(b))
print(c, type(c))

x = int(input())
y = int(input())
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)

m = int(input())
n = int(input())
temp = m
m = n
n = temp
print(m, n)

p = int(input())
q = int(input())
p = p + q
q = p - q
p = p - q
print(p, q)

num = int(input())
print("Even" if num % 2 == 0 else "Odd")

a = int(input())
b = int(input())
c = int(input())
if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

x = float(input())
y = float(input())
op = input()
if op == "+":
    print(x + y)
elif op == "-":
    print(x - y)
elif op == "*":
    print(x * y)
elif op == "/":
    print(x / y)

year = int(input())
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")

for i in range(1, 11):
    for j in range(1, 11):
        print(i * j, end=" ")
    print()

n = int(input())
fact = 1
for i in range(1, n + 1):
    fact *= i
print(fact)

n = int(input())
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

num = int(input())
s = 0
while num > 0:
    s += num % 10
    num //= 10
print(s)

num = int(input())
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print(rev)

val = input()
print("Palindrome" if val == val[::-1] else "Not Palindrome")

num = int(input())
prime = True
if num < 2:
    prime = False
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        prime = False
print("Prime" if prime else "Not Prime")

lst = []
lst.append(5)
lst.append(2)
lst.append(9)
lst.append(1)
lst.remove(2)
print(sum(lst))
print(max(lst))
print(min(lst))
lst.sort()
print(lst)

t = (1, 2, 3, 4)
print(t[0], t[1])

d = {}
d["a"] = 10
d["b"] = 20
d["c"] = 30
del d["b"]
for k, v in d.items():
    print(k, v)

s = input()
print(len(s))
print(s[1:4])
print(s[::-1])
count = 0
for ch in s:
    if ch.lower() in "aeiou":
        count += 1
print(count)

def circle(r):
    return 3.14159 * r * r

def rectangle(l, w):
    return l * w

def triangle(b, h):
    return 0.5 * b * h

print(circle(5))
print(rectangle(4, 6))
print(triangle(3, 8))
