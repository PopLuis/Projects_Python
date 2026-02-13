import random

words = ['ana','mar','mere','elicopter','dinozaur','cercei','iarba']
word = random.choice(words)
print(word)
count = 0
inp_word = input("Pleace select a word: ")
while word != inp_word:
    if inp_word != word:
        inp_word = input("Try again: ")
        count += 1


print(f"Congratulation! You have guest the word in the {count} try")

for x in words:
    for y in x:
        print(y)
    print(" \n")
