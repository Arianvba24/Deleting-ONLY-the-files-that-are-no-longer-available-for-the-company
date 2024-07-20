import os

values = list(filter(lambda x: x[-4:]=="xlsm",os.listdir(r"C:\Users\Cash\Documents\pruebas_python\proyectos\os")))

values

for value in values:
    if "REMOVE" in value:
        os.remove(fr"C:\Users\Cash\Documents\pruebas_python\proyectos\os/{value}")