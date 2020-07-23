import random

ans=random.randint(1, 10)

number=int(input("Please enter a number between 1 and 10: "))
loop=None

if number == ans:
    print("You got it right")
else:
    if number < ans:
        print("Guess higher")
    else:
        print("Guess lower: ")
    number = int(input())
    if number == ans:
        print("You got it right")
    else:
        print("You got it wrong")

