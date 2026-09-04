"""
MÓDULO DE OPERACIONES ARITMÉTICAS Y MENÚ INTERACTIVO POR TERMINAL
Repositorio: ejercicio2
Rama principal: develop

INSTRUCCIONES PARA EL EQUIPO:
--------------------------------------------------------------------------------
1. NO borres ni modifiques las funciones de otros integrantes.
2. Agrega tu función matemática en la SECCIÓN 1 (debajo de las existentes).
3. Agrega tu opción en la SECCIÓN 2 (Menú interactivo) para que el usuario pueda
   seleccionar tu operación y ver el resultado.
4. Recuerda probar el código localmente ejecutando este archivo en tu terminal:
   python aritmetica.py
--------------------------------------------------------------------------------
"""

import math

# ==============================================================================
# SECCION 1: FUNCIONES ARITMETICAS
# Cada integrante agrega aqui su funcion respetando su asignacion.
# ==============================================================================

# Suma: Katherin Dominguez
def suma(a, b):
    return a + b

# Resta: Beckerman Aguero
def resta(a, b):
    return a - b

# Multiplicacion:

# Division: Nayra Oviedo
def division(a, b):
    if b == 0:
        return None  
    return a / b

# Potencia: Guimela Cabezas
def potencia(base, exponente):
    return base ** exponente

# Raiz Cuadrada:

# Modulo (Resto de la division):

# Promedio:

# Porcentaje:

# Factorial: Luis Maturano
def factorial(n):
    if n < 0:
        return "No existe el factorial de un número negativo."
    return math.factorial(n)
# Maximo y Minimo:


# ==============================================================================
# SECCION 2: MENU INTERACTIVO POR TERMINAL
# ==============================================================================

def mostrar_menu():
    print("\n" + "=" * 40)
    print("      CALCULADORA COLABORATIVA - GRUPO")
    print("=" * 40)
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Potencia")
    print("6. Raiz Cuadrada")
    print("7. Modulo")
    print("8. Promedio")
    print("9. Porcentaje")
    print("10. Factorial")
    print("11. Maximo y Minimo")
    print("0. Salir")
    print("=" * 40)

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (0-11): ").strip()

        if opcion == "0":
            print("\n¡Gracias por usar la calculadora del grupo! Hasta luego.\n")
            break

        # ----------------------------------------------------------------------
        # LOGICA DE EJECUCION
        # Ubica el numero correspondiente a tu funcion e implementalo
        # ----------------------------------------------------------------------

        elif opcion == "1":
            print("\n--- OPERACION: SUMA ---")
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = suma(num1, num2)
            print(f"Resultado: {num1} + {num2} = {resultado}")

        elif opcion == "2":
            print("\n--- OPERACIÓN: RESTA ---")
            num1 = float(input("Ingrese el primer numero: "))
            num2 = float(input("Ingrese el segundo numero: "))
            resultado = resta(num1, num2)
            print(f"Resultado: {num1} - {num2} = {resultado}")

        elif opcion == "3":
            print("\n--- OPERACIÓN: MULTIPLICACIÓN ---")
            # TODO (Integrante 3): Pedir datos y llamar a multiplicacion(num1, num2)
            print("Función en desarrollo por el Integrante 3.")

        elif opcion == "4":
            print("\n--- OPERACIÓN: DIVISIÓN ---")
            num1 = float(input("Ingrese el numerador: "))
            num2 = float(input("Ingrese el denominador: "))
            resultado = division(num1, num2)
            if resultado is None:
                print("Error: no se puede dividir entre cero.")
            else:
                print(f"Resultado: {num1} / {num2} = {resultado}")

        elif opcion == "5":
            print("\n--- OPERACIÓN: POTENCIA ---")
            base = float(input("Ingrese el primer número base: "))
            exponente = float(input("Ingrese el segundo número exponente:"))
            resultado = potencia(base, exponente)
            print(f"Resultado: {base} ^ {exponente} = {resultado}")
          
        elif opcion == "6":
            print("\n--- OPERACIÓN: RAÍZ CUADRADA ---")
            # TODO (Integrante 6): Pedir número y llamar a raiz_cuadrada(numero)
            print("Función en desarrollo por el Integrante 6.")

        elif opcion == "7":
            print("\n--- OPERACIÓN: MÓDULO ---")
            # TODO (Integrante 7): Pedir datos y llamar a modulo(a, b)
            print("Función en desarrollo por el Integrante 7.")

        elif opcion == "8":
            print("\n--- OPERACIÓN: PROMEDIO ---")
            # TODO (Integrante 8): Pedir números separados por espacio y llamar a promedio(lista)
            print("Función en desarrollo por el Integrante 8.")

        elif opcion == "9":
            print("\n--- OPERACIÓN: PORCENTAJE ---")
            # TODO (Integrante 9): Pedir total y porcentaje, llamar a porcentaje(total, porcentaje_val)
            print("Función en desarrollo por el Integrante 9.")

        elif opcion == "10":
            print("\n--- OPERACIÓN: FACTORIAL ---")
            num = int(input("Ingrese un número entero no negativo: "))
            resultado = factorial(num)
            print(f"Resultado: {num}! = {resultado}")

        elif opcion == "11":
            print("\n--- OPERACIÓN: MÁXIMO Y MÍNIMO ---")
            # TODO (Integrante 11): Pedir números separados por espacio y llamar a maximo_minimo(lista)
            print("Función en desarrollo por el Integrante 11.")

        else:
            print("\nOpcion no valida. Por favor, selecciona un numero entre 0 y 11.")

if __name__ == "__main__":
    main()