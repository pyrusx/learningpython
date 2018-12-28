import numpy as np
import math


def f(x):
    return x ** x

def derivative(function, value):
    h = 0.00000000001  
    top = function(value + h) - function(value)
    bottom = h 
    slope = top / bottom

    return float("%.3f" % slope)


q = input('What is the type of function that you want to derive? 
                    "Exponential (E), Logarithmic (L), Trignometric (T), Polynomial (P) /n")
    if q1 == "P":
        pass

    elif q1 == "E":
        pass
    
    elif q1 == "L":
        pass
    
    elif q1 == "T":
        pass

    
    
   
         




question2 = input('What is the function itself? /n')






print(derivative(f,3))



"""if name == '__main__':
    derivative = derive(f, 2)

    print(derivative)"""



