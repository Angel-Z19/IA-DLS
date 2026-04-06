import random

# Listas con partes de la excusa
personajes = ["Un dinosaurio", "Mi gato", "Un alien", "Mi vecino"]
acciones = ["se comió", "quemó", "escondió", "lanzó al espacio"]
objetos = ["mi tarea", "mi computadora", "mi código", "las llaves"]

def generar_excusa():
    # Seleccionamos un elemento al azar de cada lista
    sujeto = random.choice(personajes)
    verbo = random.choice(acciones)
    cosa = random.choice(objetos)
    
    # Construimos la frase usando f-strings
    excusa = f"¡Lo siento! {sujeto} {verbo} {cosa}."
    return excusa

# Llamamos a la función e imprimimos el resultado
print("--- Generador de Excusas Pro ---")
print(generar_excusa())