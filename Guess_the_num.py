import random
num = int(input("Pleace enter a number: "))
if num < 0 & num > 20:
    print("The number is to big")

numar = random.randint(0, 19)

count =0
while num != numar:
    print("The number is not good! ")
    num=int(input("Enter again: "))


    count += 1


print(f"Congratulation! The number was {numar} your {count} th try")
