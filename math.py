# add implementation
from decimal import DivisionByZero


def add(x,y):
    return x+y
#subtract implementation
def subtract(x,y):
    return x-y
#multiply implementation
def multiply(x,y):
    return x*y
#divide implementation
def divide(x,y):
<<<<<<< HEAD
    return x/y
=======
    if y==0:
        return DivisionByZero
    if y>0:
        return x/y
>>>>>>> c295533... divide implimentation on bug789
