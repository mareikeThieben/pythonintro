x = int(input("Enter a number for x: "))

y = int(input("Enter number for y: "))


calculation = input("Enter+, -, *, /: ")

if calculation == "+":
    print(x + y)
elif calculation == "-":
    print(x - y)
elif calculation == "*":
    print(x * y)
elif calculation == "/":
    print(x / y)
else:
    print("You did not provide the correct math operation.")