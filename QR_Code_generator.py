import qrcode
import os

folder = "qr_codes"

if not os.path.exists(folder):
    os.makedirs(folder)

i = 1
while os.path.exists(f"{folder}/qrcode_{i}.png"):
    i += 1

data = input("Enter your url: ")

img = qrcode.make(data)
img.save(f"{folder}/qrcode_{i}.png")

print(f"QR saved as qrcode_{i}.png")
