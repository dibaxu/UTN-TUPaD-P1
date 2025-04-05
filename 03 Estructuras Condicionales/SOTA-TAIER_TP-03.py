# Trabajo Práctico n3 - Sota Taier, Pedro Antonio

#Actividad 1
edad:int = int(input("Ingrese su edad: "))
if edad > 18:
  print("Es mayor de edad")

#Actividad 2
nota:int = int(input("Ingrese su nota: "))
print("Aprobado") if nota >= 6 else print("Desaprobado")

#Actividad 3
num: int = int(input("Ingrese un número: "))
if num % 2 == 0:
  print("El número es par")
else:
  print("Por favor, ingrese un número par")

#Actividad 4
edad: int = int(input("Ingrese su edad: "))
if edad >= 30:
  print("Adulto/a")
elif edad >= 18:
  print("Adulto/a joven")
elif edad >= 12:
  print("Adolescente")
elif edad > 0:
  print("Niño/a")
else:
  print("Edad no válida")

#Actividad 5
contraseña: str = input("Ingrese la contraseña: ")
if len(contraseña) >= 8 and len(contraseña) <= 14:
  print("Ha ingresado una contraseña correcta")
else:
  print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Actividad 6
from statistics import mode, median, mean
import random
numeros_aleatorios:list = [random.randint(1, 100) for i in range(50)]
mean: float = mean(numeros_aleatorios)
median: float = median(numeros_aleatorios)
mode: float = mode(numeros_aleatorios)
print(f"Media: {mean} \nMediana: {median} \nModa: {mode}")
if mean == median == mode:
  print("Sin sesgo.")
elif mean > median > mode:
  print("Sesgo positiva.")
elif mean < median < mode:
  print("Sesgo negativo.")

#Actividad 7
palabra: str = input("Ingrese una palabra: ")
vocales: str = ("a", "e", "i", "o", "u")
if palabra.endswith(vocales):
  print(palabra+"!")
else:
  print(palabra)

#Actividad 8
nombre: str = input("Ingrese su nombre: ")
opcion: int = int(input("Ingrese 1 a 3: "))

if opcion == 1:
  print(nombre.upper())
elif opcion == 2:
  print(nombre.lower())
elif opcion == 3:
  print(nombre.title())
else:
  print("Opción no válida")

#Actividad 9
magnitud: int = int(input("Ingrese la magnitud del terremoto: "))
if magnitud >= 7:
  print("Extremo")
elif magnitud >= 6:
  print("Muy fuerte")
elif magnitud >= 5:
  print("Fuerte")
elif magnitud >= 4:
  print("Moderado")
elif magnitud >= 3:
  print("Leve")
elif magnitud > 0:
  print("Muy leve")

#Actividad 10
import sys
hemisferio: str = input("Ingrese el hemisferio (N/S): ").upper()
if hemisferio not in ("NS"): sys.exit("Valor no válido.")

año: int = int(input("Ingrese el año: "))
mes: int = int(input("Ingrese el mes: "))
dia: int = int(input("Ingrese el día: "))

if mes < 1 or mes > 12:
  print("Mes no válido")
elif dia < 1 or dia > 31:
  print("Día no válido")
elif mes == 2 and dia > 29:
  print("Día no válido")
elif mes == 2 and dia == 29 and año % 4 != 0:
  print("Día no válido")
elif mes == 4 and dia > 30:
  print("Día no válido")
elif mes == 6 and dia > 30:
  print("Día no válido")
elif mes == 9 and dia > 30:
  print("Día no válido")
elif mes == 11 and dia > 30:
  print("Día no válido")

if hemisferio == "N":
  if mes >= 3 and mes <= 5:
    print("Primavera")
  elif mes >= 6 and mes <= 8:
    print("Verano")
  elif mes >= 9 and mes <= 11:
    print("Otoño")
  else:
    print("Invierno")
elif hemisferio == "S":
  if mes >= 3 and mes <= 5:
    print("Otoño")
  elif mes >= 6 and mes <= 8:
    print("Invierno")
  elif mes >= 9 and mes <= 11:
    print("Primavera")
  else:
    print("Verano")



