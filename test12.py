import random
coin_result = random.randint(1,2)

choice = int(input("Enter your choice (head for 1 / tail for 2) : "))

if choice == 1 and coin_result == 1:
    print("It's head. You Won")
elif choice == 1 and coin_result == 2:
    print("It's tail. You Loose")
elif choice == 2 and coin_result == 1:
    print("It's head. You Loose")
elif choice == 2 and coin_result == 2:
    print("It's tail. You Won")
