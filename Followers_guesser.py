from data import ACCOUNTS
import random

a = random.choice(ACCOUNTS)
b= random.choice(ACCOUNTS)
score= 0
while a==b:
    b=random.choice(ACCOUNTS)

while True:
    print("\n-----------------------")
    print(f"[A] {a['name']} - {a['followers']:,} followers")
    print(f"[B] {b['name']} - ??? followers")
    choice=input("Enter your choice: (a or b): ").lower()
    if choice == 'a':
        corect = a['followers'] >= b['followers']
    else:
        corect = b['followers'] >= a['followers']
    if corect:
        score+=1
        print(f"Corect! score:{score}")
        a=b
        b = random.choice(ACCOUNTS)
        while b == a:
            b = random.choice(ACCOUNTS)
    else:
        print(f" Gresit! {b['name']} avea {b['followers']:,} followeri")
        print(f"Scor final: {score}")
        break


