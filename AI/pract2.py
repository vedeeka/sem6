# def sum(a, b):
#     return a + b

# def product(a, b):
#     return a * b

# def diff(a, b):
#     return a - b

# def div(a,b):
#     return a / b

# def mod(a,b):
#     return a % b


# op=input("Enter operator (+ - * / %): ")
# num1=int(input("Enter first number: "))
# num2=int(input("Enter second number: "))

# match op:
#     case "+":
#         print(sum(num1, num2))
#     case "-":
#         print(diff(num1, num2))
#     case "*":
#         print(product(num1, num2))
#     case "/":
#         print(div(num1, num2))
#     case "%":
#         print(mod(num1, num2))
#     case _:
#         print("Invalid operator")



#take a string goa college of engineering and slice the engineering part then college
# str1 = "Goa College Of Engineering"
# print("Original string:", str1)
# engineering_part = str1[15:]  
# college_part = str1[3:11]    
# #remove engineering and college part from the string use slice
# removeing_part = str1[:3] + str1[11:15]
# print("Engineering part:", engineering_part)
# print("College part:", college_part)
# print("String after removing engineering part:", removeing_part)



#find the lenght of the string
# str1 = "Goa College Of Engineering"
# length = len(str1)
# print("Length of the string:", length)

#concat two strings
# str2 = "Welcome to "
# str3 = "Goa College Of Engineering"
# concat_str = str2 + str3
# print("Concatenated string:", concat_str)

#find the vowel in a sentence
# sentence = "Goa College Of Engineering"
# vowels = "AEIOUaeiou"

# all_vowels = []
# c=0
# for char in sentence:
#     if char in vowels:
#         c+=1
#         all_vowels.append(char)

# print("Vowels in the sentence:", all_vowels) 
# print("Total number of vowels in the sentence:", c)       

#display the consonents in the sentence
# sentence = "Goa College Of Engineering"
# vowels = "AEIOUaeiou"

# all_c = []
# c=0
# for char in sentence:
#     if char not in vowels and not char.isspace():
#         c+=1
#         all_c.append(char)

# print("Consonants in the sentence:", all_c) 
# print("Total number of consonants in the sentence:", c)   



#dsa
#implement a stack using list
#stack algorithm

#assign a list
#use list as stack
#use of append to push into the list stack
#use of remove[-1] to pop from the list stack


# list_stack = []

# def push(element):
#     list_stack.append(element)
#     print(f"pushed {element} to stack.  stack data: {list_stack}")

# def pop():
#     if not list_stack:
#         print("Stack is empty. Cannot pop.")
#         return None
#     popped_element = list_stack.remove(list_stack[-1])
#     print(f"popped {popped_element} from stack.  stack: {list_stack}")
#     return popped_element

# while True:
#     match input("enter operation (push = 1/ pop = 2) and 3 to end: "):
#         case "1":
#             element = input("enter element to push: ")
#             push(element)
#         case "2":
#             pop()
#         case "3":
            
#             break


#queue


# list_stack = []

# def push(element):
#     list_stack.append(element)
#     print(f"enqueued {element} to queue.  queue data: {list_stack}")

# def pop():
#     if not list_stack:
#         print("queue is empty. Cannot dequeue.")
#         return None
#     popped_element = list_stack.remove(list_stack[0])
#     print(f"dequeue {popped_element} from queue.  queue: {list_stack}")
#     return popped_element

# while True:
#     match input("enter operation (push = 1/ pop = 2) and 3 to end: "):
#         case "1":
#             element = input("enter element to enqueue: ")
#             push(element)
#         case "2":
#             pop()
#         case "3":
            
#             break


#linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def display(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("null")


def insert_back(head, data):
    newNode = Node(data)

    if head is None:
        return newNode

    current = head
    while current.next:
        current = current.next

    current.next = newNode
    return head


def delete_value(head, value):
    if head is None:
        return None

 
    if head.data == value:
        return head.next

    current = head
    while current.next and current.next.data != value:
        current = current.next

    if current.next:
        current.next = current.next.next

    return head


head = None

while True:
    op = int(input("\nEnter 1 to add, 2 to remove, 3 to exit: "))

    if op == 1:
        n = int(input("Enter element to add: "))
        head = insert_back(head, n)
        display(head)

    elif op == 2:
        n = int(input("Enter element to delete: "))
        head = delete_value(head, n)
        display(head)

    elif op == 3:
        break
