#calculator

number = int(input("whats your first number?\n"))
calculation = input("what u want to do? \n")
number2 = int(input("choose your second number: \n"))


if calculation == '+':
    print(number + number2)

elif calculation == '-':
    print(number - number2)

elif calculation == '/':
    print(number / number2)

elif calculation == '*':
    print(number * number2)

else:
    print("choose out: +, -, / or * ")
