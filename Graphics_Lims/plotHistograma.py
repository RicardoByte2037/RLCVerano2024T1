import matplotlib.pyplot as plt

def plot_grafHist(): 
    # Datos corregidos
    frecuencias_relativas = [6, 4, 3, 2, 1.5]
    marcas_clase = [1, 2, 3, 4, 5]
    marcas_texto = [0.165, 0.495, 0.825, 1.155, 1.485]

    plt.figure(figsize=(12, 6))
    plt.bar(marcas_clase, frecuencias_relativas, width=1, edgecolor="k", color=["#37CA64", "#FF99F3", "#37C5CA", "#E74E50", "#FC8C29"])
    
    plt.xticks(marcas_clase, marcas_texto, fontsize=15, rotation=45)
    plt.xlabel("Marcas de clase", fontsize=20)
    plt.ylabel("Frecuencia relativa", fontsize=20)
    plt.title("Histograma", fontsize=25)
    plt.ylim(0, 6) 

  
    plt.grid()
    plt.show()
    