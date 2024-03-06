import modules.validaciones as v
import modules.corefiles as core

nameFile="Tienda.json"
Almacen={}

def GestorTienda():
    core.CheckFile(nameFile,Almacen)
    Tienda=core.ReadFile(nameFile)
    
    id=input("Ingrese el Id del producto\n>> ")
    nombre=input("Ingrese el nombre del producto\n>> ")
    print("Ingrese el valor unitario del producto")
    valorUnitario=v.valFloat()
    print("Ingrese el stock minimo del producto")
    stockmin=v.valInt()
    print("Ingrese el stock maximo del producto")
    stockmax=v.valInt()
    
    
    producto={
        "id":id,
        "nombre":nombre,
        "valorUnitario":valorUnitario,
        "stockmin":stockmin,
        "stockmax":stockmax,
        "stock":0
    }
    Tienda.update({id:producto})
    core.UpdateFile(nameFile,Tienda)
    pausa=input("Presiona una tecla para continuar")