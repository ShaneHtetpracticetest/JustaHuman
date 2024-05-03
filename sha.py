# print("Welcome to Xaiver Club")
# username = input("Fill your name : ")
# print("Welcome Mr." , username )
# age = int(input("Enter your age : "))

# if age >= 18:
#     print("Welcome to Xaiver Club and enjoy it")

# else:
#     print("Get the fk out of here and come back when you are 18")


# print("""                

#         Welcome from SHA's calculation 

# """)
# while True:
#     print("Enter the operation you want to perform (+, -, *, /) or 'quit' to exit:")
    
#     operation = input("Operation: ")

#     if operation.lower() == 'quit':
#         print("Exiting the calculator.")
#         break
    
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
    
#     if operation == '+':
#         result = num1 + num2
#         print("Result:", result)
#     elif operation == '-':
#         result = num1 - num2
#         print("Result:", result)
#     elif operation == '*':
#         result = num1 * num2
#         print("Result:", result)
#     elif operation == '/':
#         if num2 == 0:
#             print("Error! Division by zero.")
#         else:
#             result = num1 / num2
#             print("Result:", result)
#     else:
#         print("Invalid operation! Please enter a valid operation (+, -, *, /).")


# my_list = [1,2,1,5,2,3,5,2,4]
# print(my_list)

# my_tuple = (1,2,3,5,2,3,4,5,2,)
# print(my_tuple)

# my_set = {1,3,4,2,1,4,5,2,4}
# print(my_set)

# list_without_duplicate = set(my_list)
# print(list_without_duplicate)

# tuple_without_duplicate = set(my_tuple)
# print(tuple_without_duplicate)

# my_set = {1,2,3,4,5}
# print(my_set)

# my_tuple[0] = 10
# print(my_tuple)

# my_set.add(6)
# print(my_set)

# cc = [1,2,3,4,6,7,4,5,6]
# print(cc)
# aa = set(cc)
# print(aa)

# dd = {1,2,5,3,6,3,4,6,7}
# print(dd)

# tupple = (1,2,3,4,5)
# tupple = tupple + (6,)
# print(tupple)

# import time

# # Global variables
# stamina = 100
# sprint_cost = 10  # Stamina cost for sprinting

# # Function to decrease stamina over time
# def decrease_stamina():
#     global stamina
#     while True:
#         time.sleep(10)  # Decrease stamina every 10 seconds
#         if stamina > 0:
#             stamina -= 5  # Decrease stamina by 5 points
#         else:
#             stamina = 0

# # Function to simulate a sprint action
# def sprint():
#     global stamina
#     if stamina >= sprint_cost:
#         stamina -= sprint_cost
#     else:
#         print("Not enough stamina to sprint!")

# # Start decreasing stamina in a separate thread
# import threading
# thread = threading.Thread(target=decrease_stamina)
# thread.daemon = True
# thread.start()

# # Simulate sprint actions
# while True:
#     sprint()
#     print("Stamina:", stamina)
#     time.sleep(2)  # Simulate some delay between sprint actions


# import time

# # Global variables
# stamina = 100
# sprint_cost = 10  # Stamina cost for sprinting

# # Function to decrease stamina over time
# def decrease_stamina():
#     global stamina
#     while True:
#         time.sleep(10)  # Decrease stamina every 10 seconds
#         if stamina > 0:
#             stamina -= 5  # Decrease stamina by 5 points
#         else:
#             stamina = 0

# # Function to simulate a sprint action
# def sprint():
#     global stamina
#     if stamina >= sprint_cost:
#         stamina -= sprint_cost
#         print("Sprinting! Stamina:", stamina)
#     else:
#         print("Not enough stamina to sprint! Stopping sprint...")

# # Start decreasing stamina in a separate thread
# import threading
# thread = threading.Thread(target=decrease_stamina)
# thread.daemon = True
# thread.start()

# # Simulate sprint actions
# while True:
#     sprint()
#     if stamina == 0:
#         break  # Stop sprinting when stamina runs out
#     time.sleep(2)  # Simulate some delay between sprint actions

import time

class Character:
    def __init__(self, name, max_stamina):
        self.name = name
        self.max_stamina = max_stamina
        self.stamina = max_stamina

    def decrease_stamina(self):
        while True:
            time.sleep(10)  # Decrease stamina every 10 seconds
            if self.stamina > 0:
                self.stamina -= 5  # Decrease stamina by 5 points
            else:
                self.stamina = 0

    def sprint(self):
        if self.stamina >= sprint_cost:
            self.stamina -= sprint_cost
            print(f"{self.name} is sprinting! Stamina: {self.stamina}")
        else:
            print(f"{self.name} doesn't have enough stamina to sprint! Stopping sprint...")


sprint_cost = 10  

player = Character("Player", 100)

import threading
thread = threading.Thread(target=player.decrease_stamina)
thread.daemon = True
thread.start()

while True:
    player.sprint()
    if player.stamina == 0:
        break 
    time.sleep(2) 