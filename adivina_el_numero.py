import random
def elegir_dificultad():
    print("Selecciona un nivel de dificultad:")
    print("1. Facil (10 intentos)")
    print("2. Medio (7 intentos)")
    print("3. Dificil (5 intentos)")

    while True:
        try:
            opcion = int(input("Elige una opcion (1-3): "))
            if opcion == 1:
                return 10
            elif opcion == 2:
                return 7
            elif opcion == 3:
                return 5
            else:
                print("Por favor, elige una opcion valida 1, 2 o 3.")

        except ValueError:
            print("Entrada no valida. Por favor, introduce un numero del 1 y 3.")

def adivina_el_numero():
    print("¡Bienvenido al juego de Adivina el Numero!")
    print("He escogido un numero entre del 1 al 100. ¿Puedes adivinar cual es?")

    # Generar un numero aleatorio entre 1 y 100
    numero_secreto = random.randint(1,100)
    
    # Elegir dificultad
    intentos_restantes = elegir_dificultad()
    intentos = 0
 
    while intentos_restantes > 0:
        try:
            # Pedir al usuario que ingrese un numero
            suposicion = int(input("Introduce tu numero: "))
            intentos += 1
            intentos_restantes -= 1

            if suposicion < numero_secreto:
                print("¡Demasiado bajo! Intenta de nuevo.")
            elif suposicion > numero_secreto:
                print("¡Demasiado alto! Intentra de nuevo.")
            else:
                print(f"¡Felicidades! Adivinaste el numero{numero_secreto} en {intentos} inetntos.")
                adivinado = True
        except ValueError:
            print("Por favor, introduce un numero valido.")

# Ejecuta el juego
if __name__ == "__main__":
    adivina_el_numero()