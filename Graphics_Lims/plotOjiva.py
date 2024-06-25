import matplotlib.pyplot as plt

def plot_grafOjiva():
    marcas_clase = [0.165, 0.495, 0.825, 1.155, 1.485]
    valores_ref_eje = list(range(1, len(marcas_clase) + 1))
    facum = [30, 50, 65, 80, 100]

    datos_x_ojiva = [0] + valores_ref_eje
    datos_y_ojiva = [0] + facum

    plt.figure(figsize=(15, 5))
    plt.plot(datos_x_ojiva, datos_y_ojiva, 
             linewidth=3, 
             color="#1C2833",
             linestyle="--", 
             marker="v", 
             markersize=10, 
             markerfacecolor="#EB7AF5", 
             markeredgecolor="#003DA2",
             markeredgewidth=1.5) 

    plt.xticks(valores_ref_eje, marcas_clase, fontsize=10)
    plt.xlabel("Marcas de clase", fontsize=15)
    plt.ylabel("Frecuencia acumulada", fontsize=15)
    plt.title("Ojiva", fontsize=20)
    plt.grid()
    plt.show()

