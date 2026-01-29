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



# n=int(input("Enter first number: "))
# m=int(input("Enter second number: "))
# k=int(input("Enter second number: "))

# if(n>m and n>k):
#     print(n," n is largest")
# elif(m>n and m>k):
#     print(m, " m is largest")
# else:
#     print(k," k is largest")


# sum=0

# for i in range(0,10):
#     n=int(input("Enter  number: "))
#     sum+=n
#     print("sum= ",sum)



# fac=1
# n=int(input("Enter the number :"))
# for i in range(1,n+1):
#     fac*=i
# print("factorial= ",fac)


top=0
structure={}

#for multiple students
for student in range(3):
    structure[student] = {}
    print(f"Enter details for student {student+1}:")
    structure[student]["IT1"]={}
    structure[student]["Name"]=input("Enter student name: ")
    print("Enter student details in IT1:")


    for i in range(3):
        subject=input("Enter subject name: ")
        marks=int(input("Enter marks: "))
        structure[student]["IT1"][subject]=marks

    print("Entered details for It2")
    structure[student]["IT2"]={}

    for i in range(3):
        subject=input("Enter subject name: ")
        marks=int(input("Enter marks: "))
        structure[student]["IT2"][subject]=marks

    print("Entered details for It3")
    structure[student]["IT3"]={}

    for i in range(3):
        subject=input("Enter subject name: ")
        marks=int(input("Enter marks: "))
        structure[student]["IT3"][subject]=marks

    total=0
# two highest marks as per the each subject in together 3 ITs
    for subject in structure[student]["IT1"].keys():
        marks_it1 = structure[student]["IT1"][subject]
        marks_it2 = structure[student]["IT2"][subject]
        marks_it3 = structure[student]["IT3"][subject]

        highest_marks = sorted([marks_it1, marks_it2, marks_it3], reverse=True)[:2]
        avg_marks = sum(highest_marks) / 2
        total += avg_marks
        print(f"Average of top two marks in {subject} across IT1, IT2, and IT3: {avg_marks}")
        print(f"Top two marks in {subject} across IT1, IT2, and IT3: {highest_marks}")

    print(f"Total average marks for student {structure[student]['Name']}: {total}")

    if(top<total):
        top=total
        toppers=structure[student]['Name']

    #finding the top 

        
print(f"The topper is {toppers} with total average marks: {top}")      






