while True:
    a = float(input("First number: "))
    b = float(input("Second number: "))
    op = input("Operation (+ - * /) or q to quit: ")

    if op == "q":
        break
    elif op == "+":
        print(a + b)
    elif op == "-":
        print(a - b)
    elif op == "*":
        print(a * b)
    elif op == "/":
        print(a / b if b != 0 else "Division by zero!")
    else:
        print("Invalid operation")
