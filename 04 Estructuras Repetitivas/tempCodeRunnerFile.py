num:int = int(input("Ingrese un número entero: "))
num_invertido:int = 0

while num > 0:
  num_invertido = num_invertido * 10 + num % 10
  num = num // 10

print("h")
print(num_invertido)