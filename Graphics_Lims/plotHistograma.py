import matplotlib.pyplot as plt
import numpy as np

def plot_grafHist(frecuencias_relativas, marcas_clase, marcas_texto): 
    plt.figure(figsize=(12, 6))
    x = np.arange(len(marcas_clase))  # Creamos un arreglo de indices para las columnas
    width = 0.5  # Ancho de las columnas
    
    plt.bar(x, frecuencias_relativas, width, edgecolor="k", color=["#37CA64", "#FF99F3", "#37C5CA", "#E74E50", "#FC8C29"])
    
    plt.xticks(x, marcas_texto, fontsize=15, rotation=45)
    plt.xlabel("Marcas de clase", fontsize=20)
    plt.ylabel("Frecuencia relativa", fontsize=20)
    plt.title("Histograma", fontsize=25)
    plt.ylim(0, max(frecuencias_relativas) * 1.1) 

    plt.grid()
    plt.show()
    