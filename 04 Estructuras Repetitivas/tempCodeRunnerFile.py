suma: int = 0
num: int = int(input("Ingrese un número entero positivo: "))
for i in range(num + 1):
  suma += i
print("La suma de los números entre 0 y", num, "es:", suma)