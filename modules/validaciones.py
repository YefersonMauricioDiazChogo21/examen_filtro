from tabulate import tabulate
import os

def valInt():
    try: 
        x=int(input(">> "))
        return x
    except ValueError:
        print("Solo se aceptan numeros, ingrese nuevamente")
        return valInt()
    
def valFloat():
    try: 
        x=float(input(">> "))
        return x
    except ValueError:
        print("Solo se aceptan numeros, ingrese nuevamente")
        return valFloat()
    