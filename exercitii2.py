n = int(input("n = "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")

lista = [1, 5, 3, 9, 2]

print("Suma:", sum(lista))
print("Maxim:", max(lista))
print("Minim:", min(lista))

n = input("n = ")

if n == n[::-1]:
    print("Palindrom")
else:
    print("Nu este palindrom")
