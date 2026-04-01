import random

def easy_chance(winning_num):
    chance = 10
    print("You will have 10 chances to win")
    while chance > 0:
        gh_num = int(input("Enter the number: "))
        if gh_num > winning_num:
            print("The number is lower!")
            chance -= 1
        elif gh_num < winning_num:
            print("The number is higher!")
            chance -= 1
        else:
            print("Congratulations!")
            print(f"You guessed the number on the {11 - chance}th try")
            break
    print("You have used all of your tries!")


def hard_chance(winning_num):
    chance = 5
    print("You will have 5 chances to win")
    while chance > 0:
        gh_num = int(input("Enter the number: "))
        if gh_num > winning_num:
            print("The number is lower!")
            chance -= 1
        elif gh_num < winning_num:
            print("The number is higher!")
            chance -= 1
        else:
            print("Congratulations!")
            print(f"You guessed the number on the {6 - chance}th try")
            break
    print("You have used all of your tries!")


winning_num = random.randint(1, 100)
print("Welcome to the Guess the Number game!")
print("Choose difficulty (easy or hard): ")
difficulty = input()
if difficulty == "easy":
    easy_chance(winning_num)
if difficulty == "hard":
    hard_chance(winning_num)
