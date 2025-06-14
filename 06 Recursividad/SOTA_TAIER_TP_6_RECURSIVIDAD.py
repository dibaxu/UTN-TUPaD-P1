# 1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa función para calcular y mostrar en pantalla el factorial de todos los números enteros entre 1 y el número que indique el usuario

def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número: "))
print(f"El factorial de {numero} es: {factorial(numero)}")

# 2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario especifique.

def fibonacci(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

posicion = int(input("Ingrese la posición de Fibonacci: "))
print(f"El valor en la posición {posicion} de la serie de Fibonacci es: {fibonacci(posicion)}")
print("Serie de Fibonacci hasta la posición", posicion, ":")
for i in range(posicion + 1):
    print(fibonacci(i), end=" ")

# 3) Crea una función recursiva que calcule la potencia de un número base elevado a un exponente, utilizando la fórmula 𝑛 𝑚 = 𝑛 ∗ 𝑛 (𝑚−1). Prueba esta función en un algoritmo general.

def potencia(base: int, exponente: int) -> int:
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base = int(input("\nIngrese la base: "))
exponente = int(input("Ingrese el exponente: "))
print(f"{base} elevado a {exponente} es: {potencia(base, exponente)}")

# 4) Crear una función recursiva en Python que reciba un número entero positivo en base decimal y devuelva su representación en binario como una cadena de texto.
def decimal_a_binario(n: int) -> str:
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

numero_decimal = int(input("\nIngrese un número entero positivo decimal: "))
print(f"El número {numero_decimal} en binario es: {decimal_a_binario(numero_decimal)}")

#5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.

def es_palindromo(palabra: str) -> bool:
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])
palabra = input("\nIngrese una palabra sin espacios ni tildes: ").lower()
if es_palindromo(palabra):
    print(f"{palabra} es un palíndromo.")
else:
    print(f"{palabra} no es un palíndromo.")


# 6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un número entero positivo y devuelva la suma de todos sus dígitos.

def suma_digitos(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n % 10 + suma_digitos(n // 10)

numero = int(input("\nIngrese un número entero positivo: "))
print(f"La suma de los dígitos de {numero} es: {suma_digitos(numero)}")

# 7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al último nivel con un solo bloque. 
# Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el nivel más bajo y devuelva el total de bloques que necesita para construir toda la pirámide. 

def contar_bloques(n: int) -> int:
    if n<=0:
        return 0
    else:
        return n + contar_bloques(n-1)

n_bloques = int(input("\nIngrese el número de bloques en el nivel más bajo: "))
print(f"El total de bloques necesarios para construir la pirámide es: {contar_bloques(n_bloques)}")

# 8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces aparece ese dígito dentro del número.
def contar_digito(numero: int, digito:int) -> int:
    if numero == 0:
        return 0
    else:
        return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)
    
numero = int(input("\nIngrese un número: "))
digito = int(input("Ingrese un dígito (entre 0 y 9): "))
print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en el número {numero}.")