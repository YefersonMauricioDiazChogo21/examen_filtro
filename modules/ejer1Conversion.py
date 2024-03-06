import modules.validaciones as v
# En este modulo vamos a convertir de pesos a alguno de los tipos especificados a continuacion
# 1 yen = 26.30 pesos
# 1 dólar = 3944 pesos
# 1 euro = 4279 pesos
def ConversionDePesos():
    v.os.system("clear")
    titulo=[["|      CONVERSIONES DE PESOS      |"]]
    print(v.tabulate(titulo,tablefmt="heavy_grid"))
    print("Ingrese el valor en pesos a convertir")
    valor=v.valFloat()
    bandera=True
    while bandera:
        opciones="""
    1. CONVERTIR A YENES
    2. CONVERTIR A DOLARES
    3. CONVERTIR A EUROS
            """
        print(opciones)
        opc=v.valInt()
        if opc==1:
            resultado=valor*1/26.30
            conv="Yenes"
            bandera=False
        elif opc==2:
            resultado=valor*1/3944
            conv="Dolares"
            bandera=False
        elif opc==3:
            resultado=valor*1/4279
            conv="Euros"
            bandera=False
        else:
            print("Opcion no valida")
    print(f"{valor} pesos colombianos equivalen a {resultado} {conv}")
    pausa=input("Presiona una tecla para continuar")
            
def ConversionDeEuro():
    v.os.system("clear")
    titulo=[["|      CONVERSIONES DE EUROS      |"]]
    print(v.tabulate(titulo,tablefmt="heavy_grid"))
    print("Ingrese el valor en euros a convertir")
    valor=v.valFloat()
    resultado=valor*4279
    print(f"{valor} euros equivalen a {resultado} pesos colombianos")
    pausa=input("Presiona una tecla para continuar")