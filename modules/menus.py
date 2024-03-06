import modules.validaciones as v
import modules.ejer1Conversion as c
import modules.ejer2Usuarios as u
import modules.ejer3Tienda as t


def MenuConversion():
    
    bandera=True
    while bandera:
        v.os.system("clear")
        titulo=[["|      CONVERSIONES DE MONEDAS      |"]]
        print(v.tabulate(titulo,tablefmt="heavy_grid"))
        opciones="""
    1. REALIZAR CONVERSION DE PESOS
    2. REALIZAR CONVERSION DE EUROS
    3. SALIR
        """
        print(opciones)
        opc=v.valInt()
        
        if opc==1:
            c.ConversionDePesos()
        elif opc==2:
            c.ConversionDeEuro()
        elif opc==3:
            print("Bye")
            bandera=False
        else:
            print("Opcion incorrecta")
            
def MenuUsuarios():
    
    bandera=True
    while bandera:
        v.os.system("clear")
        titulo=[["|      GESTION DE USUARIOS      |"]]
        print(v.tabulate(titulo,tablefmt="heavy_grid"))
        opciones="""
    1. AÑADIR USUARIO
    2. SALIR
        """
        print(opciones)
        opc=v.valInt()
        if opc==1:
            u.GestionUsuarios()
        elif opc==2:
            print("Bye")
            bandera=False
        else:
            print("Opcion incorrecta")

def MenuTienda():
    
    bandera=True
    while bandera:
        v.os.system("clear")
        titulo=[["|      GESTION DE TIENDA      |"]]
        print(v.tabulate(titulo,tablefmt="heavy_grid"))
        opciones="""
    1. AÑADIR PRODUCTO
    2. SALIR
        """
        print(opciones)
        opc=v.valInt()
        if opc==1:
            t.GestorTienda()
        elif opc==2:
            print("Bye")
            bandera=False
        else:
            print("Opcion incorrecta")      
    

def MenuPrincipal():
    v.os.system("clear")
    bandera=True
    while bandera:
        
        titulo=[["|      EXAMEN FINAL DE PYTHON      |"]]
        print(v.tabulate(titulo,tablefmt="heavy_grid"))
        opciones="""
    1. CONVERSION DE MONEDA
    2. GETOR DE USUARIOS
    3. GETOR DE TIENDA
    4. GETOR DE NOMINA
    5. SALIR
        """
        print(opciones)
        opc=v.valInt()
        
        if opc==1:
            MenuConversion()
        elif opc==2:
            MenuUsuarios()
        elif opc==3:
            MenuTienda()
        elif opc==4:
            pass
        elif opc==5:
            print("Bye")
            bandera=False
        else:
            print("Opcion incorrecta")