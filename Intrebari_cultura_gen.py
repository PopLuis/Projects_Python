score = 0

print("Care este capitala Romaniei?")
print("A) Cluj")
print("B) Bucuresti")
print("C) Iasi")
print("D) Timisoara")

r = input("Raspuns: ")

if r == "B" or r == "b":
    print("Corect!")
    score += 1
else:
    print("Gresit!")

print("\nCat face 2 + 2 % 2?")
print("A) 3")
print("B) 4")
print("C) 5")
print("D) 22")

r = input("Raspuns: ")

if r == "A" or r == "a  ":
    print("Corect!")
    score += 1
else:
    print("Gresit!")

# Intrebarea 3
print("\n3. Care planeta este cea mai apropiata de Soare?")
print("A) Venus")
print("B) Marte")
print("C) Mercur")
print("D) Jupiter")
r = input("Raspuns: ")

if r == "C" or r == "c":
    print("Corect!")
    score += 1
else:
    print("Gresit!")

# Rezultat final
print("\nScor final:", score, "/ 3")
