import json
import modules.validaciones as v
BASE="data/"

def CheckFile(Archivo,diccionario:dict):
    if not(v.os.path.isfile(BASE+Archivo)):
        with open(BASE+Archivo,"w+") as create:
            json.dump(diccionario,create,indent=4)

def UpdateFile(Archivo,diccionario:dict):
    with open(BASE+Archivo,"w+") as update:
            json.dump(diccionario,update,indent=4)
            
def ReadFile(Archivo):
    with open(BASE+Archivo,"r") as read:
            return json.loads(read.read())