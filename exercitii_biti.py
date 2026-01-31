n = 13  # 1101 în binar
k = 2   # verificăm bitul 2

if n & (1 << k):
    print(f"Bitul {k} este 1")
else:
    print(f"Bitul {k} este 0")
n = 8   # 1000 în binar
k = 1   # vrem să setăm bitul 1

n = n | (1 << k)  # OR pe biți
print(f"Numărul după setarea bitului {k}: {n}")

n = 15  # 1111 în binar
k = 2   # vrem să ștergem bitul 2

n = n & ~(1 << k)  # AND cu complement
print(f"Numărul după resetarea bitului {k}: {n}")
n = 5  # 0101 în binar
k = 0  # inversăm bitul 0

n = n ^ (1 << k)  # XOR pe biți
print(f"Numărul după inversarea bitului {k}: {n}")
n = 3  # 0011 în binar

print(f"Shift la stânga cu 2: {n << 2}")  # 3 * 2^2 = 12
print(f"Shift la dreapta cu 1: {n >> 1}") # 3 / 2 = 1
