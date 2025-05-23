""" 
Actividades 
1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea. 
"""
# Actividad 1
for i in range(101):
  print(i)

"""
2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
dígitos que contiene. 
"""
num: int = int(input("Ingrese un número entero: "))
cont_d: int = 0
while num > 0:
    num = num // 10
    cont_d += 1
print("Cantidad de dígitos:", cont_d)
# Alternativa con str
print("Cantidad de dígitos:", len(str(num)))

"""
3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
dados por el usuario, excluyendo esos dos valores.
"""
num1: int = int(input("Ingrese el primer número: "))
num2: int = int(input("Ingrese el segundo número: "))
suma: int = 0

for i in range(num1 + 1, num2):
  suma += i
print("La suma de los números entre", num1, "y", num2, "es:", suma)

"""
4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
un 0.
"""
suma:int = 0
num:int = int(input("Ingrese un número entero (0 para salir): "))
while num != 0:
  suma += num
  num = int(input("Ingrese un número entero (0 para salir): "))

print("La suma de los números ingresados es:", suma)

""""
5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
"""
import random
num_aleatorio:int = random.randint(0, 9)
intentos:int = 1
num_usuario:int = int(input("Adivina el número entre 0 y 9: "))
while num_usuario != num_aleatorio:
  intentos += 1
  print("Número incorrecto. Intenta de nuevo.")
  num_usuario = int(input("Adivina el número entre 0 y 9: "))

print(f"El número era {num_aleatorio}. Intentos: {intentos}.")

"""
6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
entre 0 y 100, en orden decreciente. 
"""
for i in range(100, -1, -1):
  if i % 2 == 0:
    print(i)

"""
7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.
"""
suma: int = 0
num: int = int(input("Ingrese un número entero positivo: "))
for i in range(num + 1):
  suma += i
print("La suma de los números entre 0 y", num, "es:", suma)

"""
8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
menor, pero debe estar preparado para procesar 100 números con un solo cambio). 
"""
num_pares: int = 0
num_impares: int = 0
num_positivos: int = 0
num_negativos: int = 0
num: int = 0
for i in range(100):
  num = int(input("Ingrese un número entero: "))
  if num % 2 == 0:
    num_pares += 1
  else:
    num_impares += 1
  
  if num > 0:
    num_positivos += 1
  elif num < 0:
    num_negativos += 1

print("Números pares:", num_pares)
print("Números impares:", num_impares)
print("Números positivos:", num_positivos)
print("Números negativos:", num_negativos)


"""
9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
poder procesar 100 números cambiando solo un valor). 
"""
promedio: float = 0.0
suma: int = 0

for i in range(100):
  num = int(input("Ingrese un número entero: "))
  suma += num

promedio = suma / 100
print("La media de los números ingresados es:", promedio)

"""
10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745. 
"""
num:int = int(input("Ingrese un número entero: "))
num_invertido:int = 0

while num > 0:
  num_invertido = num_invertido * 10 + num % 10
  num = num // 10

print(num_invertido)
