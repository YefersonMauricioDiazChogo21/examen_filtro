import modules.validaciones as v

def GestionUsuarios():
    diccionario={}
    v.os.system("clear")
    titulo=[["|      AGREGAR UN USUARIO      |"]]
    print(v.tabulate(titulo,tablefmt="heavy_grid"))
    print("Ingrese el Id del usuario")
    id=v.valInt()
    nombres=input("Ingrese los nombres del usuario\n")
    apellidos=input("Ingrese los apeliidos del usuario\n")
    dirección=input("Ingrese la direccion del usuario\n")
    ciudad=input("Ingrese la ciudad del usuario\n")
    longitud=input("Ingrese la longitud de ubicacion del usuario\n")
    latitud=input("Ingrese la latitud de ubicacion usuario\n")
    email=input("Ingrese el email del usuario\n")
    edad=input("Ingrese la edad del usuario\n")
    ocupación=input("Ingrese la ocupacion del usuario\n")
    
    usuario={
        "id":id,
        "nombres":nombres,
        "apellidos":apellidos,
        "ubicación":{
            "dirección":dirección,
            "ciudad":ciudad,
            "longitud":longitud,
            "latitud":latitud},
        "email":email,
        "edad":edad,
        "ocupación":ocupación
    }
    diccionario.update({id:usuario})
    print(diccionario[id])
    usuariomostrar=[[diccionario[id]["id"],diccionario[id]["nombres"],diccionario[id]["edad"]]]
    print(v.tabulate(usuariomostrar,headers=["ID","NOMBRE","EDAD"],tablefmt="heavy_grid"))
    pausa=input("Presiona una tecla para continuar")
                    