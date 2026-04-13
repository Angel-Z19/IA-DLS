from models import Problem
from algorithms import depth_limited_search
from visualize import animar_recorrido

mapa_mexico = {
    # Baja California
    "Tijuana": [("Tecate", 52), ("Rosarito", 20)],
    "Rosarito": [("Tijuana", 20), ("Ensenada", 85)],
    "Tecate": [("Tijuana", 52), ("Mexicali", 135), ("Ensenada", 100)],
    "Ensenada": [
        ("Rosarito", 85),
        ("Tecate", 100),
        ("San Felipe", 246),
        ("San Quintin", 185),
    ],
    "Mexicali": [("Tecate", 135), ("San Luis Rio Colorado", 80), ("San Felipe", 197)],
    "San Felipe": [("Mexicali", 197), ("Ensenada", 246), ("Guerrero Negro", 394)],
    "San Quintin": [("Ensenada", 185), ("Guerrero Negro", 425)],
    "Guerrero Negro": [
        ("San Quintin", 425),
        ("San Felipe", 394),
        ("Santa Rosalia", 220),
    ],
    "Santa Rosalia": [("Guerrero Negro", 220), ("Mulege", 63)],
    "Mulege": [("Santa Rosalia", 63), ("Ciudad Constitucion", 283)],
    "Ciudad Constitucion": [("Mulege", 283), ("San Carlos", 61), ("La Paz", 210)],
    "San Carlos": [("Ciudad Constitucion", 61)],
    "La Paz": [
        ("Ciudad Constitucion", 210),
        ("San Jose del Cabo", 201),
        ("Cabo San Lucas", 157),
    ],
    "San Jose del Cabo": [("La Paz", 201), ("Cabo San Lucas", 38)],
    "Cabo San Lucas": [("San Jose del Cabo", 38), ("La Paz", 157)],
    # Sonora
    "San Luis Rio Colorado": [("Mexicali", 80), ("Sonoyta", 203)],
    "Sonoyta": [
        ("San Luis Rio Colorado", 203),
        ("Puerto Penasco", 98),
        ("Caborca", 149),
    ],
    "Puerto Penasco": [("Sonoyta", 98), ("Caborca", 176)],
    "Caborca": [("Sonoyta", 149), ("Puerto Penasco", 176), ("Santa Ana", 107)],
    "Santa Ana": [
        ("Caborca", 107),
        ("Nogales", 107),
        ("Cananea", 125),
        ("Hermosillo", 171),
    ],
    "Nogales": [("Santa Ana", 107), ("Cananea", 99)],
    "Cananea": [("Nogales", 99), ("Santa Ana", 125), ("Agua Prieta", 86)],
    "Agua Prieta": [("Cananea", 86), ("Janos", 160), ("Moctezuma", 199)],
    "Moctezuma": [("Agua Prieta", 199), ("Hermosillo", 178), ("Yécora", 257)],
    "Yécora": [("Moctezuma", 257), ("Hermosillo", 278), ("Ciudad Cuauhtemoc", 309)],
    "Hermosillo": [
        ("Santa Ana", 171),
        ("Guaymas", 135),
        ("Moctezuma", 178),
    ],
    "Guaymas": [("Hermosillo", 135), ("Ciudad Obregon", 130)],
    "Ciudad Obregon": [("Guaymas", 130)],
    # Chihuahua
    "Janos": [("Agua Prieta", 160), ("Ciudad Juarez", 212), ("Flores Magon", 173)],
    "Ciudad Juarez": [("Janos", 212), ("Villa Ahumada", 125)],
    "Villa Ahumada": [("Ciudad Juarez", 125), ("Flores Magon", 93), ("Sueco", 85)],
    "Flores Magon": [
        ("Villa Ahumada", 93),
        ("Sueco", 60),
        ("Ciudad Cuauhtemoc", 211),
        ("Janos", 173),
    ],
    "Sueco": [("Flores Magon", 60), ("Villa Ahumada", 85), ("Chihuahua", 158)],
    "Chihuahua": [
        ("Sueco", 158),
        ("Delicias", 87),
        ("Parral", 225),
        ("Ciudad Cuauhtemoc", 105),
        ("Ojinaga", 379),
    ],
    "Ojinaga": [("Chihuahua", 379)],
    "Delicias": [("Chihuahua", 87), ("Ciudad Jimenez", 139)],
    "Ciudad Jimenez": [("Delicias", 139), ("Parral", 215)],
    "Parral": [("Chihuahua", 225), ("Ciudad Jimenez", 215)],
    "Ciudad Cuauhtemoc": [("Chihuahua", 105), ("Flores Magon", 211), ("Yécora", 309)],
}

# Coordenadas relativas (X, Y) basadas en el mapa visual
posiciones_mapa = {
    # Baja California (Norte a Sur)
    'Tijuana': (0, 10.2), 'Rosarito': (-0.5, 9.3), 'Tecate': (1, 10.4),
    'Mexicali': (2, 10.5), 'Ensenada': (0, 8.3), 'San Felipe': (1.7, 7.9),
    'San Quintin': (0, 6.9), 'Guerrero Negro': (1, 6),
    'Santa Rosalia': (1.6, 4.5), 'Mulege':(1.9, 3), 'Ciudad Constitucion': (1.5, 1),
    'San Carlos': (0.6, 0.4),'La Paz': (2, -0.5), 'San Jose del Cabo': (2.6, -1.5),
    'Cabo San Lucas' : (1.6, -2.8),

    # Sonora (Oeste a Este)
    'San Luis Rio Colorado': (3.4, 10.4), 'Sonoyta': (4.7, 9.6),
    'Puerto Penasco': (4, 8), 'Caborca': (5.8, 6.7),
    'Santa Ana': (6.7, 5.77), 'Nogales': (6.6, 9.4),
    'Cananea': (7.7, 6.7), 'Agua Prieta': (8.6, 9),
    'Hermosillo': (7, 2.4), 'Guaymas': (5.9, 0.35), 'Ciudad Obregon': (7.4, -1.5),
    'Moctezuma': (8.2, 3.16), 'Yécora': (8.8, 1.15),
    'Navojoa': (7, 4), 'Alamos': (7.5, 3.8),

    # Chihuahua
    'Janos': (9.3, 8.5), 'Ciudad Juarez': (11.7, 10.3), 'Villa Ahumada': (12.1, 8.3),
    'Sueco': (12.4, 6.3), 'Flores Magon': (10, 6),
    'Ojinaga': (13.8, 7.8), 'Chihuahua': (12.8, 2.8),
    'Ciudad Cuauhtemoc': (11.3, 1), 'Delicias': (13.4, 0.7),
    'Camargo': (12, 4.5), 'Ciudad Jimenez': (13.7, -2.1),
    'Parral': (12.1, -3.4), 'Guadalupe y Calvo': (10, 3.5),
}


inicio = 'Tijuana'
meta = 'Ciudad Juarez'
limite = 20


problema = Problem(inicio, meta, mapa_mexico)

resultado = depth_limited_search(problema, limite)

animar_recorrido(mapa_mexico, resultado, posiciones = posiciones_mapa)