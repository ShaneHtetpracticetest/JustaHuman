answer = 70
guess = int(input("Enter your guess within 0 to 100 : "))
if guess > answer:
    print("Wrong Guess. Try Smaller")
elif guess < answer:
    print("Wrong Guess. Try Bigger")
elif guess == answer:
    print("Bingo")
else:
    print("invalid Input. Try Again")