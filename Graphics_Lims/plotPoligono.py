import matplotlib.pyplot as plt 

def plot_grafPoligono():
    marcas_clase = [0.165, 0.495, 0.825, 1.155, 1.485]
    valores_ref_eje = list(range(1, len(marcas_clase) + 1))
    fr = [30, 20, 15, 15, 20]

    datos_x_poligono = [0] + valores_ref_eje + [valores_ref_eje[-1] + 1]
    datos_y_poligono = [0] + fr + [0]

    plt.figure(figsize=(15, 5))
    plt.plot(datos_x_poligono, datos_y_poligono, 
             linewidth=3, 
             color="#1C2833", 
             linestyle="--", 
             marker="o", 
             markersize=10, 
             markerfacecolor="#EB7AF5", 
             markeredgecolor="#003DA2",
             markeredgewidth=1.5)
    
    plt.xticks(valores_ref_eje, marcas_clase, fontsize=10)
    plt.xlabel("Marcas de clase", fontsize=15)
    plt.ylabel("Frecuencia relativa", fontsize=15)
    plt.title("Polígono de frecuencias", fontsize=20)
    plt.grid()
    plt.show() 


