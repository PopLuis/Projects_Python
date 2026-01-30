n = 6
f = 1

for i in range(1, n+1):
    f *= i

print(f)

def fact(n):
    return 1 if n <= 1 else n * fact(n-1)

print(fact(6))

def factorial(n):
    if n == 0:  # Base case
        return 1
    else:       # Recursive case
        return n * factorial(n - 1)

print(factorial(5))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))
