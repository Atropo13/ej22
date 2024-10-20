from datetime import date
from ejercicio2 import *


def muestra_variaciones_temperatura_fechas(ruta_csv, fecha_inicial, fecha_final):
    variaciones = lee_variaciones_temperatura(ruta_csv)
    
    # Tenemos que dividir la lista de tuplas en dos
    # listas:
    valores_x = []
    valores_y = []
    for v in variaciones:
        if (fecha_inicial == None or v.fecha >= fecha_inicial) and\
           (fecha_final == None or v.fecha <= fecha_final):
            valores_x.append(v.fecha)
            valores_y.append(v.variacion)

    plt.title("Variación de temperaturas medias del planeta")
    plt.plot(valores_x, valores_y)
    plt.show()


if __name__ == '__main__':
    muestra_variaciones_temperatura_fechas(
        "data/monthly_csv.csv", date(1880, 1, 1), date(1910, 1, 1))
    
    muestra_variaciones_temperatura_fechas(
         "data/monthly_csv.csv", None, date(1980, 1, 1))
    muestra_variaciones_temperatura_fechas(
         "data/monthly_csv.csv", date(1980, 1, 1), None)