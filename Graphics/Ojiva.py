import matplotlib.pyplot as plt

def plot_ojiva(marcas_clase, valores_ref_eje, fa, fr, facum, sabores):
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
    plt.xlabel("Sabores", fontsize=15)
    plt.ylabel("Frecuencia acumulada", fontsize=15)
    plt.title("Ojiva", fontsize=20)
    plt.grid()
    plt.show()
    