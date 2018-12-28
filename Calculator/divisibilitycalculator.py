import math


def add(num1, num2):
     return num1 + num2

def sub(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Divide by Zero Error!")


def main():
    num1 = int((input("What do you want to do? 1. Check if a number is odd/even "
                      "2. Check if one number is divisible by another number "
                      "3. Use calculator\n")))
    if num1 == 1:
        num2 = int(input("Type in a number to check if it is odd, even, and/or divisible by 4.\n"))
        if num2 % 4 == 0:
            print(str(num2) + " is even and divisible by 4!")
            return main2()

        elif num2 % 2 == 0:
            print(str(num2) + " is an even number!")
            return main2()

        else:
            print(str(num2) + " is an odd number!")
            return main2()

    elif num1 == 2:
        num3 = int(input("What is the dividend?\n"))
        num4 = int(input("what is the divisor?\n"))
        num5 = num3 / num4
        num6 = math.floor(num3 / num4)
        if (num5) == 0:
            print(str(num3) + " is divisible by " + str(num4))
            return main2()
        else:
            print(str(num3) + " is not divisible by " + str(num4) + ". "
                    + str(num4) + " goes into the number " + str(num3)
                    + " " + "only " + str(num6) + " times. The remainder is "
                    + str(num3 % num4) + ".")
            return main2()
    elif num1 == 3:
        
        def calc():
            operation = input("What operation do you want to perform?"
                                " 1. Addition 2. Subtraction 3. Multiplication"
                                " 4. Division\n")
            num1 = int(input("What is the first number?\n"))
            num2 = int(input("What is the second number?\n"))

            operation_without_space = operation.strip()

            if operation_without_space == "1":
                print((add(num1, num2)))
                return main2()

            elif operation_without_space == "2":
                print((sub(num1, num2)))
                return main2()
            elif operation_without_space == "3":
                print((mult(num1, num2)))
                return main2()
            elif operation_without_space == "4":
                print((div(num1, num2)))
                return main2()
            else:
                print("Invalid operation")
                return main2()

        calc()
    else:
        print("Invalid response. Please type 1, 2, or 3, depending on what you want to check.")
        main()


def main2():
    print('Thank you for using my calculator! The calculator will now load up so you can use it.\n')
    return main()


main()
