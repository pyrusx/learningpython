def divisors():
    myNumber1 = int(input('Type in a number to find its divisors. \n'))

    for i in range(1, (myNumber1 + 1)):    
        if (myNumber1 % i) == 0:
            print(i)