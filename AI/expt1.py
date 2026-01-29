#add two numbers
# def add(a, b):
#     return a + b


# n=int(input("Enter first number: "))
# m=int(input("Enter second number: "))

# result = add(n, m)
# print(result)
# print("The sum is:", result)


# n=int(input("Enter first number: "))
# m=int(input("Enter second number: "))
# result = n + m
# print("The sum is:", result)


# n=int(input("Enter first number: "))
# if(n%2==0):
#     print("Even")
# else:
#     print("Odd")



n=int(input("Enter first number: "))
m=int(input("Enter second number: "))
k=int(input("Enter second number: "))

if(n>m and n>k):
    print(n," n is largest")
elif(m>n and m>k):
    print(m, " m is largest")
else:
    print(k," k is largest")
