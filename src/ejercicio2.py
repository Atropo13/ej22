from ejercicio1 import lee_variaciones_temperatura
from matplotlib import pyplot as plt
pip install matplotlib

import matplotlib.dates as mdates

def muestra_variaciones_temperatura(ruta_csv):
    variaciones = lee_variaciones_temperatura(ruta_csv)
    
    # Tenemos que dividir la lista de tuplas en dos
    # listas:
    valores_x = []
    valores_y = []
    for v in variaciones:
        valores_x.append(v.fecha)
        valores_y.append(v.variacion)

    plt.title("Variación de temperaturas medias del planeta")
    plt.plot(valores_x, valores_y)
    plt.show()


if __name__ == '__main__':
    muestra_variaciones_temperatura("data/monthly_csv.csv")