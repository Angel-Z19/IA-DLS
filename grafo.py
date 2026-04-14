grafo = {
    #Baja California
    'Tijuana' : [('Rosarito',20), ('Tecate', 52)],
    'Rosarito' : [('Ensenada', 85),('Tijuana', 20)],
    'Tecate' : [('Ensenada', 100), ('Tijuana', 52), ('Mexicali', 135)],
    'Ensenada' :[('Rosarito', 85), ('Tecate', 100), ('San Quintin', 185), ('San Felipe', 246)],
    'Mexicali' :[('Tecate', 135), ('San Felipe', 197), ('San Luis Rio Colorado', 80)],
    #Baja California Sur
    'San Quintin' : [('Ensenada', 185), ('Guerrero Negro', 425)],
    'San Felipe' : [('Ensenada', 246), ('Mexicali', 197), ('Guerrero Negro', 394)],
    'Guerrero Negro' : [('San Quintin', 425), ('San Felipe', 394), ('Santa Rosalia', 220)],
    'Santa Rosalia' : [('Guerrero Negro', 220), ('Mulege', 283)],
    'Mulege' : [('Santa Rosalia', 63), ('Ciudad Constitucion', 283)],
    'Ciudad Constitucion' : [('Mulege', 283), ('San Carlos', 61), ('La Paz', 210)],
    'San Carlos' : [('Ciudad Constitucion', 61)],
    'La Paz' : [('Ciudad Constitucion', 210), ('Cabo San Lucas', 157), ('San Jose del Cabo'), 201],
    'Cabo San Lucas' : [('La Paz', 157), ('San Jose del Cabo', 38)],
    'San Jose del Cabo' : [('La Paz', 201), ('Cabo San Lucas', 38)],
    #Sonora creo
    'San Luis Rio Colorado' : [('Mexicali', 80), ('Sonoyta', 203)],
    'Sonoyta' : [('San Luis Rio Colorado', 203), ('Puerto Penasco', 98), ('Caborca', 149)],
    'Puerto Penasco' : [('Sonoyta', 98), ('Caborca', 176)],
    'Caborca' : [('Puerto Penasco', 176), ('Sonoyta', 149), ('Santa Ana', 107)],
    'Santa Ana' : [('Nogales', 107), ('Hermosillo', 171), ('Cananea', 125)],
    'Nogales' : [('Santa Ana', 107), ('Cananea', 99)],
    'Hermosillo' : [('Santa Ana', 171), ('Guaymas', 135), ('Moctezuma', 178), ('Yecora', 278)],
    'Guaymas' : [('Hermosillo', 135), ('Ciudad Obregon', 130)],
    'Ciudad Obregon' : [('Guaymas', 130), ('Los Mochis', 232)],
    'Los Mochis' : [('Ciudad Obregon', 232), ('Guasave', 62)],
    'Guasave' : [('Los Mochis', 62)],
    'Cananea' : [('Santa Ana', 125), ('Nogales', 99), ('Agua Prieta', 86)],
    'Agua Prieta' : [('Cananea', 86), ('Moctezuma', 199), ('Janos', 160)],
    'Moctezuma' : [('Hermosillo', 178), ('Agua Prieta', 199), ('Yecora', 257)],
    'Yecora' : [('Hermosillo', 278), ('Moctezuma', 257), ('Ciudad Cuauhtemoc', 309)],
    







}