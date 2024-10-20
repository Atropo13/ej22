import csv
from collections import namedtuple
from datetime import datetime

VariacionTemperatura = namedtuple('VariacionTemperatura','fecha variacion')

def lee_variaciones_temperatura(ruta):
    with open(ruta, encoding='utf-8') as f:
        lector = csv.reader(f)
        next(lector) # next "consume" un dato de la secuencia
        res = []
        for fecha, variacion in lector:
            fecha = datetime.strptime(fecha, "%d/%m/%Y").date() # Tengo que convertir la fecha a date!
            variacion = float(variacion)
            tupla = VariacionTemperatura(fecha, variacion)
            res.append(tupla)
        return res

if __name__ == "__main__":        
    datos = lee_variaciones_temperatura("data/monthly_csv.csv")
    print("Primer elemento:", datos[0])
    print("Último elemento:", datos[-1])
    