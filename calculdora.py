def suma(a, b):
    return a + b 

def resta(a, b):
    return a - b 

def multiplicacion (a, b):
    return a * b 

def division (a, b):
    if b == 0: "Error: No se pude dividir entre cero"
    return a / b 

def calculadora():

    print("=== Calculadora Basica ===")
    print("Opciones:")
    print("1: Suma")
    print("2: Resta")
    print("3: Multiplicacion")
    print("4: Division")
    print("5: Salir")

    while True:
        try:
            opcion = int(input("\nElige una operacion (1-5): "))
            
            if opcion == 5:
                print("¡Hasta Luego!")
                break

            if opcion in [1, 2, 3, 4]:
                num1 = float(input("Ingresa el primer numero: "))
                num2 = float(input("Ingresa el segundo numero: "))

                if opcion == 1:
                    resultado = suma (num1, num2)
                    print(f"Resultado de la suma {resultado}")
                elif opcion == 2:
                    resultado = resta(num1, num2)
                    print(f"Resultado de la resta: {resultado}")
                elif opcion == 3:
                    resultado = multiplicacion (num1, num2)
                    print(f"Resultado de la multiplicacion: {resultado}")
                elif opcion == 4:
                    resultado = division (num1, num2)
                    print(f"Resultado de la division: {resultado}")
            else: 
                print("Opcion no valida. Intenta de nuevo.")
        except ValueError:
            print("Entrada no valida. Por favor, ingresa un numero.")

if __name__ == "__main__":
    calculadora()