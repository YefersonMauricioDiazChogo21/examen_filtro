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
    
def valiCargo():
    opciones="""
    1. Almacenista
    2. Jefe IT
    3. Administrador
    4. Mensajero
    5. Gerente
    """
    print(opciones)
    op=valInt()
    if op==1:
        cargo="Almacenista"
    elif op==2:
        cargo="Jefe IT"
    elif op==3:
        cargo="Administrador"
    elif op==4:
        cargo="Mensajero"
    elif op==5:
        cargo="Gerente"
    else:
        print("Opcion no valida")
        return valiCargo()
    
    return cargo
        
def valDia():  
    dia=valInt()
    if dia>31 or dia<0:
        print("Dia no valido")
        return valDia()
    else:
        return dia

def valMes():  
    print("Ingrese el mes")
    mes=valInt()
    if mes>12 or mes<0:
        print("Mes no valido")
        return valMes()
    else:
        if mes==1:
            nameMes="Enero"
        elif mes==2:
            nameMes="Febrero"
        elif mes==3:
            nameMes="Marzo"
        elif mes==4:
            nameMes="Abril"
        elif mes==5:
            nameMes="Mayo"
        elif mes==6:
            nameMes="Junio"
        elif mes==7:
            nameMes="Julio"
        elif mes==8:
            nameMes="Agosto"
        elif mes==9:
            nameMes="Septiembre"
        elif mes==10:
            nameMes="Octubre"
        elif mes==11:
            nameMes="Noviembre"
        elif mes==12:
            nameMes="Diciembre"
        return mes, nameMes

def valiFecha():
    print("Ingrese el dia ")
    dia=valDia()
    mes, nameMes=valMes()
    print("Ingrese el año")
    año=valInt()
    fecha=str(dia)+"/"+str(mes)+"/"+str(año)
    return fecha, nameMes

def valKey(diccionario:dict):
    try:
        x=str(input(">> "))
        diccionario["empleados"][x]
        return x
    except ValueError:
        print("Empleado no existente")
        return valKey(diccionario)
