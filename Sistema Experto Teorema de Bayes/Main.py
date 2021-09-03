from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import font
import os.path as path
import json

listaSintomas=[]
COVID={}
FARINGITIS={}
GRIPE={}
INFLUENZA={}
NEUMONIA={}
probCOVID=0.0
probFARINGITIS=0.0
probGRIPE=0.0
probINFLUENZA=0.0
probNEUMONIA=0.0

data = {
            "NOMBRE": "NEUMONIA",
            "Dolor en el pecho al respirar o toser": {
                "Prob":0.8
            },
            "Desorientacion": {
                "Prob": 0.25
            },
            "Tos con flema ":{
                "Prob": 0.35
            },
            "Fatiga":{
                "Prob": 0.4
            },
            "Fiebre":{
                "Prob": 0.35
            },
            "Dificultad para respirar":{
                "Prob": 0.85
            },
            "Vomitos y diarrea": {
                "Prob": 0.15
            },
            "Prob": 0.2
        }

with open("ENFERMEDADES.json", 'r') as jsonTrastorno:
    ENFERMEDADES= json.load(jsonTrastorno)

ENFERMEDADES["ENFERMEDAD"].append(data)

with open("ENFERMEDADES.json", 'w') as jsonTrastorno:
    json.dump(ENFERMEDADES,jsonTrastorno,indent=4)

with open("ENFERMEDADES.json", 'r') as jsonTrastorno:
    ENFERMEDADES= json.load(jsonTrastorno)

COVID = ENFERMEDADES["ENFERMEDAD"][0]
FARINGITIS = ENFERMEDADES["ENFERMEDAD"][1]
GRIPE = ENFERMEDADES["ENFERMEDAD"][2]
INFLUENZA = ENFERMEDADES["ENFERMEDAD"][3]
NEUMONIA = ENFERMEDADES["ENFERMEDAD"][4]

global vCriterios
vCriterios = Tk()
fuente=font.Font(family="Helvetica",size=16,weight="bold")
vCriterios.title("Criterios")
vCriterios.resizable(False,False)

global boolFiebre
boolFiebre = BooleanVar()
chkFiebre = Checkbutton(vCriterios, text="Fiebre", variable=boolFiebre,font=fuente)
chkFiebre.grid(row=0, column=0, sticky="w")

global boolTos
boolTos = BooleanVar()
chkTos = Checkbutton(vCriterios, text="Tos", variable=boolTos,font=fuente)
chkTos.grid(row=1, column=0, sticky="w")

global boolDificultadpararespirar
boolDificultadpararespirar = BooleanVar()
chkDificultadpararespirar = Checkbutton(vCriterios, text="Dificultad para respirar", variable=boolDificultadpararespirar,font=fuente)
chkDificultadpararespirar.grid(row=2, column=0, sticky="w")

global boolFatiga
boolFatiga = BooleanVar()
chkFatiga = Checkbutton(vCriterios, text="Fatiga", variable=boolFatiga,font=fuente)
chkFatiga.grid(row=3, column=0, sticky="w")

global boolDolordecuerpo
boolDolordecuerpo = BooleanVar()
chkDolordecuerpo = Checkbutton(vCriterios, text="Dolor de cuerpo", variable=boolDolordecuerpo,font=fuente)
chkDolordecuerpo.grid(row=4, column=0, sticky="w")

global boolDolordecabeza
boolDolordecabeza = BooleanVar()
chkDolordecabeza = Checkbutton(vCriterios, text="Dolor de cabeza", variable=boolDolordecabeza,font=fuente)
chkDolordecabeza.grid(row=5, column=0, sticky="w")

global boolPérdidadOlfatoGusto
boolPérdidadOlfatoGusto = BooleanVar()
chkPérdidadOlfatoGusto = Checkbutton(vCriterios, text="Pérdida del olfato o el gusto", variable=boolPérdidadOlfatoGusto,font=fuente)
chkPérdidadOlfatoGusto.grid(row=6, column=0, sticky="w")

global boolDolordeGarganta
boolDolordeGarganta = BooleanVar()
chkDolordeGarganta = Checkbutton(vCriterios, text="Dolor de Garganta", variable=boolDolordeGarganta,font=fuente)
chkDolordeGarganta.grid(row=7, column=0, sticky="w")

global boolCongestion
boolCongestion = BooleanVar()
chkCongestion = Checkbutton(vCriterios, text="Congestion", variable=boolCongestion,font=fuente)
chkCongestion.grid(row=8, column=0, sticky="w")

global boolVomitosyDiarrea
boolVomitosyDiarrea = BooleanVar()
chkVomitosyDiarrea = Checkbutton(vCriterios, text="Vomitos y Diarrea", variable=boolVomitosyDiarrea,font=fuente)
chkVomitosyDiarrea.grid(row=9, column=0, sticky="w")

global boolDolorPecho
boolDolorPecho = BooleanVar()
chkDolorPecho = Checkbutton(vCriterios, text="Dolor en el pecho al respirar o toser", variable=boolDolorPecho,font=fuente)
chkDolorPecho.grid(row=10, column=0, sticky="w")

global boolDesorientacion
boolDesorientacion = BooleanVar()
chkDesorientacion = Checkbutton(vCriterios, text="Desorientación", variable=boolDesorientacion,font=fuente)
chkDesorientacion.grid(row=11, column=0, sticky="w")

global boolTosconflema
boolTosconflema = BooleanVar()
chkTosconflema = Checkbutton(vCriterios, text="Tos con flema", variable=boolTosconflema,font=fuente)
chkTosconflema.grid(row=12, column=0, sticky="w")

global boolSequedad
boolSequedad = BooleanVar()
chkSequedad = Checkbutton(vCriterios, text="Sequedad de la garganta", variable=boolSequedad,font=fuente)
chkSequedad.grid(row=13, column=0, sticky="w")

global boolErupciones
boolErupciones = BooleanVar()
chkErupciones = Checkbutton(vCriterios, text="Erupciones cutáneas", variable=boolErupciones,font=fuente)
chkErupciones.grid(row=14, column=0, sticky="w")

global boolAmigdalas
boolAmigdalas = BooleanVar()
chkAmigdalas = Checkbutton(vCriterios, text="Amígdalas rojas e inflamadas", variable=boolAmigdalas,font=fuente)
chkAmigdalas.grid(row=15, column=0, sticky="w")

global boolVozRonca
boolVozRonca = BooleanVar()
chkVozRonca = Checkbutton(vCriterios, text="Voz Ronca", variable=boolVozRonca,font=fuente)
chkVozRonca.grid(row=16, column=0, sticky="w")

def diagnostico():
    #Se obtienen los sintomas seleccionados
    if boolFiebre.get():
        listaSintomas.append("Fiebre")
    
    if boolTos.get():
        listaSintomas.append("Tos")

    if boolDificultadpararespirar.get():
        listaSintomas.append("Dificultad para respirar")

    if boolFatiga.get():
        listaSintomas.append("Fatiga")
    
    if boolDolordecuerpo.get():
        listaSintomas.append("Dolor de cuerpo")
    
    if boolDolordecabeza.get():
        listaSintomas.append("Dolor de cabeza")

    if boolPérdidadOlfatoGusto.get():
        listaSintomas.append("Perdida del olfato o el gusto")

    if boolDolordeGarganta.get():
        listaSintomas.append("Dolor de garganta")

    if boolCongestion.get():
        listaSintomas.append("Congestion")

    if boolVomitosyDiarrea.get():
        listaSintomas.append("Vomitos y diarrea")
    
    if boolDolorPecho.get():
        listaSintomas.append("Dolor en el pecho al respirar o toser")
    
    if boolDesorientacion.get():
        listaSintomas.append("Desorientacion")
    
    if boolTosconflema.get():
        listaSintomas.append("Tos con flema")
    
    if boolSequedad.get():
        listaSintomas.append("Sequedad de la garganta")

    if boolErupciones.get():
        listaSintomas.append("Erupciones cutaneas")
    
    if boolAmigdalas.get():
        listaSintomas.append("Amigdalas rojas e inflamadas")
    
    if boolVozRonca.get():
        listaSintomas.append("Voz ronca")

    covid=1.0
    faringitis=1.0
    gripe=1.0
    influenza=1.0
    neumonia=1.0
    print(listaSintomas)
    for elem in listaSintomas: #Se calculan las probabilidades condicionales P(S |Ei), donde S es el conjunto de sintomas y Ei la enfermedad correspondiente
        print(elem)
        try:
            covid*=COVID[elem]["Prob"]
            print(COVID[elem])
        except KeyError:
            covid*=.15

        try:
            faringitis*=FARINGITIS[elem]["Prob"]
            print(FARINGITIS[elem])
        except KeyError:
            faringitis*=.15

        try:
            gripe*=GRIPE[elem]["Prob"]
            print(GRIPE[elem])
        except KeyError:
            gripe*=.15
        
        try:
            influenza*=INFLUENZA[elem]["Prob"]
            print(INFLUENZA[elem])
        except KeyError:
            influenza*=.15

        try:
            neumonia*=NEUMONIA[elem]["Prob"]
            print(NEUMONIA[elem])
        except KeyError:
            neumonia*=.15
    
    #Se multiplica P(S |Ei) * P(Ei)
    covid*=COVID["Prob"]

    faringitis*=FARINGITIS["Prob"]

    gripe*=GRIPE["Prob"]

    influenza*=FARINGITIS["Prob"]

    neumonia*=NEUMONIA["Prob"]

    
    print("PARTE DE ABAJO: ",(covid+faringitis+gripe+influenza+neumonia))


    #Se calcula el Teorema de Bayes por cada Enfermedad
    probCOVID = covid/(covid+faringitis+gripe+influenza+neumonia)

    probFARINGITIS = faringitis/(covid+faringitis+gripe+influenza+neumonia)
    
    probGRIPE = gripe/(covid+faringitis+gripe+influenza+neumonia)

    probINFLUENZA = influenza/(covid+faringitis+gripe+influenza+neumonia)
    
    probNEUMONIA = neumonia/(covid+faringitis+gripe+influenza+neumonia)
    
    
    def myFunc(e):
      return e['prob']

    #Se obtiene la probabilidad mayor ordenandolas de mayor a menor
    probList=[{'prob':probCOVID,'Enfermedad':'COVID'},{'prob':probFARINGITIS,'Enfermedad':'FARINGITIS'},{'prob':probGRIPE,'Enfermedad':'GRIPE'},{'prob':probINFLUENZA,'Enfermedad':'INFLUENZA'},{'prob':probNEUMONIA,'Enfermedad':'NEUMONIA'}]
    probList.sort(key=myFunc,reverse=TRUE)

    print(probList)

    print("probabilidad de COVID: ",probCOVID)
    print("probabilidad de FARINGITIS: ",probFARINGITIS)
    print("probabilidad de GRIPE: ",probGRIPE)
    print("probabilidad de INLUENZA: ",probINFLUENZA)
    print("probabilidad de NEUMONIA: ",probNEUMONIA)

    probFinal=int(probList[0]['prob']*100)

    #Imprime el resultado con un messagebox
    text = "Puede que tenga "+probList[0]['Enfermedad']+" con una probabilidad de: "+str(probFinal)+"%"
    messagebox.showinfo(message=text, title="Resultados")

    listaSintomas.clear()

    boolFiebre.set(False)
    boolTos.set(False)
    boolDificultadpararespirar.set(False)
    boolFatiga.set(False)
    boolDolordecuerpo.set(False)
    boolDolordecabeza.set(False)
    boolPérdidadOlfatoGusto.set(False)
    boolDolordeGarganta.set(False)
    boolCongestion.set(False)
    boolVomitosyDiarrea.set(False)
    boolDolorPecho.set(False)
    boolDesorientacion.set(False)
    boolTosconflema.set(False)
    boolSequedad.set(False)
    boolErupciones.set(False)
    boolAmigdalas.set(False)
    boolVozRonca.set(False)


btnDiagnostico = ttk.Button(vCriterios, text="Diagnosticar",command=diagnostico)
btnDiagnostico.grid(row=17, column=0)
vCriterios.mainloop()


