import modules.validaciones as v
import modules.corefiles as core

nameFile="Nomina.json"
Registro={
    "empleados":{},
    "colillas":{}
}

def AñadirUsuario():
    v.os.system("clear")
    titulo=[["|      AGREGAR UN USUARIO      |"]]
    print(v.tabulate(titulo,tablefmt="heavy_grid"))
    core.CheckFile(nameFile,Registro)
    Nomina=core.ReadFile(nameFile)
    id=input("Ingrese el Id del Empleado\n>> ")
    nombre=input("Ingrese el nombre del Empleado\n>> ")
    print("Seleccione el cargo del empleado")
    cargo=v.valiCargo() #(Almacenista, Jefe IT, Administrador, Mensajero, Genrente)
    print("Ingrese el salario base del Empleado")
    salario= v.valInt()
    
    Empleado={
        "id":id,
        "nombre":nombre,
        "cargo":cargo,
        "salario":salario
    }
    Nomina["empleados"].update({id:Empleado})
    core.UpdateFile(nameFile,Nomina)

def CalcularNomina():
    v.os.system("clear")
    titulo=[["|      CALCULAR NOMINA      |"]]
    print(v.tabulate(titulo,tablefmt="heavy_grid"))
    v.os.system("clear")
    Nomina=core.ReadFile(nameFile)
    print("Ingrese el Id del trabajador")
    id=v.valKey(Nomina)
    print("Ingrese el numero de dias trabajados por el empleado")
    diasTrabajados=v.valDia()
    print("Ingrese la fecha del pago")
    fecha, mes=v.valiFecha()
    print("Ingrese el numero de horas extras trabajas")
    horasExtras=v.valInt()
    print("Ingrese el valor de la dueda en cafeteria del Empleado")
    descuentoxCafeteria=v.valInt()
    print("Ingrese el valor de la cuota de prestamo del Empleado")
    cuotaPrestamo=v.valInt()
    sueldo=Nomina["empleados"][id]["salario"]
    valorExtras=horasExtras*5500
    valorDia=sueldo/30
    totalPago=(diasTrabajados*valorDia)+valorExtras-cuotaPrestamo-descuentoxCafeteria
    ColillaPago={
        "Mes_Pagado":mes,
        "Fecha_Pago" :fecha,  #(dd/mm/yyyy)
        "Sueldo_Base":sueldo,
        "Valor_Total_Extras":valorExtras,
        "Cuota_Prestamo":cuotaPrestamo,
        "Descuento_X_Cafeteria":descuentoxCafeteria,
        "Total_A_Pagar":totalPago
    }
    Nomina["colillas"].update({id:ColillaPago})
    core.UpdateFile(nameFile,Nomina)

def ColillasPago():
    v.os.system("clear")
    titulo=[["|      BUSCAR COLILLA DE PAGO      |"]]
    print(v.tabulate(titulo,tablefmt="heavy_grid"))
    v.os.system("clear")
    Nomina=core.ReadFile(nameFile)
    print("Ingrese el Id del Empleado")
    id=v.valKey(Nomina)
    for i in Nomina["colillas"]:
        if id==i:
            colilla=[]
            for i in Nomina["colillas"][id]:
                lista=[i,Nomina["colillas"][id][i]]
                colilla.append(lista)
            break
    print(v.tabulate(colilla,headers=["COLILLA",id],tablefmt="rounded_grid"))
    pausa=input("Presiona una tecla para continuar")

def TotalNominasPagas():
    v.os.system("clear")
    titulo=[["|      TOTAL PAGO POR CONCEPTO NOMINA      |"]]
    print(v.tabulate(titulo,tablefmt="heavy_grid"))
    v.os.system("clear")
    Nomina=core.ReadFile(nameFile)
    TotalPagoNominas=0
    for i in Nomina["colillas"]:
        TotalPagoNominas+=Nomina["colillas"][i]["Total_A_Pagar"]
    print(f"El total pagado por concepto nominas es de {TotalPagoNominas}")
    pausa=input("Presiona una tecla para continuar")
        
