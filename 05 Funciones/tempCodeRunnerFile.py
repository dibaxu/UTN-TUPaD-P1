def calcular_promedio(a:int, b:int, c:int) -> float:
    return (a + b + c) / 3

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
c = int(input("Ingrese el tercer número: "))
promedio = calcular_promedio(a, b, c)
print(f"El promedio de {a}, {b} y {c} es: {promedio}")