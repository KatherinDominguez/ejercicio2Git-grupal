# Calculadora Colaborativa - Grupo

Calculadora interactiva por terminal desarrollada de forma colaborativa. Cada integrante del equipo implementó una operación matemática diferente y la integró al menú principal.

**Repositorio:** ejercicio2  
**Rama principal:** develop

---

## Descripción

Este proyecto es una calculadora de operaciones aritméticas básicas y avanzadas con un menú interactivo en la terminal. El usuario puede seleccionar la operación deseada, ingresar los datos correspondientes y obtener el resultado de forma inmediata.

El código está organizado en dos secciones principales:

1. **Funciones aritméticas** — Cada función implementada por un integrante del equipo.
2. **Menú interactivo** — Interfaz por terminal que permite elegir y ejecutar las operaciones.

---

## Operaciones disponibles

| Opción | Operación              | Descripción                                      | Autor(es)              |
|--------|------------------------|--------------------------------------------------|------------------------|
| 1      | Suma                   | Suma de dos números                              | Katherin Dominguez     |
| 2      | Resta                  | Resta de dos números                             | Beckerman Aguero       |
| 3      | Multiplicación         | Producto de dos números                          | Vanessa Flores         |
| 4      | División               | División de dos números (maneja división por cero) | Nayra Oviedo         |
| 5      | Potencia               | Eleva un número a una potencia                   | Guimela Cabezas        |
| 6      | Raíz Cuadrada          | Calcula la raíz cuadrada (valida números negativos) | -                    |
| 7      | Módulo                 | Resto de la división (valida división por cero)  | Mirko                  |
| 8      | Promedio               | Calcula el promedio de una lista de números      | Dajhana                |
| 9      | Porcentaje             | Calcula el porcentaje de un valor                | -                      |
| 10     | Factorial              | Calcula el factorial de un número entero         | Luis Maturano          |
| 11     | Máximo y Mínimo        | Encuentra el valor máximo y mínimo de una lista  | Ximena Condo           |
| 0      | Salir                  | Cierra la aplicación                             | -                      |

---

## Requisitos

- Python 3.6 o superior
- Módulo estándar `math` (incluido en Python)

No se requieren dependencias externas.

---

## Cómo ejecutar

1. Clona o descarga el repositorio.
2. Abre una terminal en la carpeta del proyecto.
3. Ejecuta el archivo principal:

```bash
python aritmetica.py
```

o, si usas Python 3 explícitamente:

```bash
python3 aritmetica.py
```

---

## Ejemplo de uso

```
========================================
      CALCULADORA COLABORATIVA - GRUPO
========================================
1. Suma
2. Resta
3. Multiplicacion
4. Division
5. Potencia
6. Raiz Cuadrada
7. Modulo
8. Promedio
9. Porcentaje
10. Factorial
11. Maximo y Minimo
0. Salir
========================================
Selecciona una opción (0-11): 1

--- OPERACION: SUMA ---
Ingrese el primer número: 15
Ingrese el segundo número: 7
Resultado: 15.0 + 7.0 = 22.0
```

---

## Estructura del código

```
aritmetica.py
│
├── SECCIÓN 1: Funciones aritméticas
│   ├── suma(a, b)
│   ├── resta(a, b)
│   ├── multiplicacion(a, b)
│   ├── division(a, b)
│   ├── potencia(base, exponente)
│   ├── raiz_cuadrada(numero)
│   ├── modulo(a, b)
│   ├── promedio(valores)
│   ├── porcentaje(total, porcentaje_val)
│   ├── factorial(n)
│   └── maximo_minimo(valores)
│
└── SECCIÓN 2: Menú interactivo
    ├── mostrar_menu()
    └── main()
```

---

## Instrucciones para el equipo

1. **No borres ni modifiques** las funciones de otros integrantes.
2. Agrega tu función matemática en la **SECCIÓN 1** (debajo de las existentes).
3. Agrega tu opción en la **SECCIÓN 2** (Menú interactivo) para que el usuario pueda seleccionarla.
4. Prueba el código localmente ejecutando:

```bash
python aritmetica.py
```

---

## Notas importantes

- Las operaciones de **división**, **módulo** y **raíz cuadrada** incluyen validaciones para evitar errores (división por cero o raíces de números negativos).
- El **factorial** solo acepta números enteros no negativos.
- El **promedio** y **máximo/mínimo** reciben una lista de valores separados por espacios.

---

## Licencia

Este proyecto es de uso educativo y colaborativo para el curso / ejercicio grupal.