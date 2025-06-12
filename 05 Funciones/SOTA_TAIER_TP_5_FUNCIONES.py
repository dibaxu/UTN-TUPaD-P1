import math
# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.
def imprimir_hola_mundo():
    print("Hola Mundo!")
imprimir_hola_mundo()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado.
def llamada_saludar_usuario(nombre:str):
    return f"Hola, {nombre}!"
print(llamada_saludar_usuario("Juan"))

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]. Pedir los datos al usuario y llamar a esta función con los valores ingresados.
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = int(input("Ingrese su edad: "))
residencia = input("Ingrese su residencia: ")

def informacion_personal(nombre:str, apellido:str, edad:int, residencia:str):
    return f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}."

print(informacion_personal(nombre, apellido, edad, residencia))

#4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.
radio = float(input("Ingrese el radio del círculo: "))
def calcular_area_circulo(radio: float) -> float:    
    pi = math.pi 
    return math.pi * (radio ** 2)

def calcular_perimetro_circulo(radio: float) -> float:
    pi = math.pi  
    return 2 * pi * radio
print(f"El área del círculo es: {calcular_area_circulo(radio)}")
print(f"El perímetro del círculo es: {calcular_perimetro_circulo(radio)}")

# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.
def segundos_a_horas(segundos:int) -> float:
    return segundos / 3600

segundos = int(input("Ingrese la cantidad de segundos: "))
print(f"{segundos} segundos son {segundos_a_horas(segundos)} horas.")

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.
def tabla_multiplicar(numero: int) -> None:
    for i in range (1, 11):
        print(f"{numero} x {i} = {numero * i}")

numero = int(input("Ingrese un número: "))
tabla_multiplicar(numero)

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
def operaciones_basicas(a: int, b: int) -> tuple:
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"
    return (suma, resta, multiplicacion, division)

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
resultado = operaciones_basicas(a, b)
print(f"Resultados:\nSuma: {resultado[0]}\nResta: {resultado[1]}\nMultiplicación: {resultado[2]}\nDivisión: {resultado[3]}")

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
def calcular_imc(peso:float, altura:float) -> float:
    return peso / (altura ** 2)

peso = float(input("Ingrese peso: "))
altura = float(input("Ingrese altura: "))
imc = calcular_imc(peso, altura)
print(f"El índice de masa corporal (IMC) es: {imc:.2f}")

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
def celsius_a_fahrenheit(celsius: float) -> float:
    return (celsius * 9/5) + 32

celsius = float(input("Ingrese la temperatura en Celsius: "))
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")

# 10.Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.
def calcular_promedio(a:int, b:int, c:int) -> float:
    return (a + b + c) / 3

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))
promedio = calcular_promedio(a, b, c)
print(f"El promedio de {a}, {b} y {c} es: {promedio}")
