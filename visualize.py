import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from models import Node

def animar_recorrido(grafo_dict, resultado, posiciones):
    if not isinstance(resultado, Node):
        print(f"No se puede animar: {resultado}")
        return

    camino = resultado.get_path()
    
    costos_paso_a_paso = []
    temp_node = resultado
    while temp_node:
        costos_paso_a_paso.append(temp_node.path_cost)
        temp_node = temp_node.parent
    costos_paso_a_paso = costos_paso_a_paso[::-1]

    # Configuramos la figura
    fig, ax = plt.subplots(figsize=(18, 11))
    G = nx.DiGraph()
    for origen, conexiones in grafo_dict.items():
        for destino, km in conexiones:
            G.add_edge(origen, destino)

    # Dibujamos el mapa estático de fondo (muy tenue)
    nx.draw(G, posiciones, with_labels=True, node_color='lightblue', 
            node_size=900,  font_size=7, edge_color='silver', ax=ax)

    # Creamos el "viajero" (usaremos un emoji de carro o persona)
    viajero = ax.text(0, 0, '🚗', fontsize=20, ha='center', va='center', zorder=10)
    
    # Línea que marcará el rastro
    rastro_x, rastro_y = [], []
    linea_rastro, = ax.plot([], [], color='orange', linewidth=3, alpha=0.6)

    def actualizar(i):
        ciudad_actual = camino[i]
        distancia_acumulada = costos_paso_a_paso[i]
        x, y = posiciones[ciudad_actual]
        
        # Movemos el icono
        viajero.set_position((x, y))
        
        # Actualizamos el rastro
        rastro_x.append(x)
        rastro_y.append(y)
        linea_rastro.set_data(rastro_x, rastro_y)
        
        # Resaltamos el nodo donde está parado
        nx.draw_networkx_nodes(G, posiciones, nodelist=[ciudad_actual], 
                               node_color='orange', node_size=700, ax=ax)
        
        ax.set_title(f"Recorriendo: {ciudad_actual} | Paso {i+1} de {len(camino)} | Distancia recorrida: {distancia_acumulada} km", fontsize=15)
        return viajero, linea_rastro

    # frames = número de ciudades en el camino
    # interval = 600ms (puedes bajarlo a 300 para que vaya más rápido)

    # 1. Ajustar los límites de los ejes (ajusta según tus coordenadas mínimas y máximas)
    # Si tus X van de 0 a 15 y Y de 0 a 10:
    ax.set_xlim(-2, 15) 
    ax.set_ylim(-4, 14)

    # 3. Eliminar los márgenes automáticos que deja Matplotlib
    plt.subplots_adjust(left=0, right=1, top=0.9, bottom=0)

    ani = animation.FuncAnimation(fig, actualizar, frames=len(camino), 
                                  interval=800, repeat=False)

    plt.axis('off')
    plt.show()