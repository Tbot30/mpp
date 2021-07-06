# Fizz if %3 Buzz if %5 FizzBuzz wiht both
number = int(input("wut is your number 0, ..\n"))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)


# Code from site (official?)

#for fizzbuzz in range(number):
#    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
#        print("fizzbuzz")
#        continue
#    elif fizzbuzz % 3 == 0:
#        print("fizz")
#        continue
#    elif fizzbuzz % 5 == 0:
#        print("buzz")
#        continue
#    print(fizzbuzz)