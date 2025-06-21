# 1) Dado el diccionario precios_frutas
# Añadir las siguientes frutas con sus respectivos precios:
# ● Naranja = 1200
# ● Manzana = 1500
# ● Pera = 2300
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450 }
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

# 2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
# ● Banana = 1330
# ● Manzana = 1700
# ● Melón = 2800

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

# 3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.
frutas: list = list(precios_frutas.keys())
print(frutas)

# 4) Escribí un programa que permita almacenar y consultar números telefónicos.
# • Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
# • Luego, pedí un nombre y mostrale el número asociado, si existe.

contactos: dict = {}
for i in range(5):
    nombre = input("Ingrese el nombre del contacto: ")
    numero = input("Ingrese el número de teléfono: ")
    contactos[nombre] = numero

nombre_consulta = input("Ingrese el nombre del contacto a consultar: ")
if nombre_consulta in contactos:
    print(f"El número de {nombre_consulta} es: {contactos[nombre_consulta]}")
else:
    print(f"El contacto {nombre_consulta} no existe.")

# 5) Solicita al usuario una frase e imprime:
# • Las palabras únicas (usando un set).
# • Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")
palabras:list = frase.split()
palabras_unicas: set = set(palabras)
contador_palabras :dict = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

print(f"Palabras únicas: {palabras_unicas}")
print(f"Cantidad de veces que aparece cada palabra: {contador_palabras}")

# 6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

alumnos: dict[str, tuple[float]] = {}
for i in range(3):
    nombre = input("Ingrese el nombre del alumno: ")
    nota_1 = float(input("Ingrese la primera nota: "))
    nota_2 = float(input("Ingrese la segunda nota: "))
    nota_3 = float(input("Ingrese la tercera nota: "))
    notas = (nota_1, nota_2, nota_3)
    alumnos[nombre] = notas

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {alumno} es: {promedio}")

# 7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1 y Parcial 2:
# • Mostrá los que aprobaron ambos parciales.
# • Mostrá los que aprobaron solo uno de los dos.
# • Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).
parcial_1: set = {1, 2, 3, 4, 5}
parcial_2: set = {4, 5, 6, 7, 8}
print(f"Estudiantes que aprobaron ambos parciales: {parcial_1.intersection(parcial_2)}")
print(f"Estudiantes que aprobaron solo uno de los dos: {parcial_1.symmetric_difference(parcial_2)}")
print(f"Lista total de estudiantes que aprobaron al menos un parcial: {parcial_1.union(parcial_2)}")

# 8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.Permití al usuario:
# • Consultar el stock de un producto ingresado.
# • Agregar unidades al stock si el producto ya existe.
# • Agregar un nuevo producto si no existe.

products: dict[str, int] = {}
def consultar_stock(producto: str) -> int:
    if producto in products:
        return products[producto]
    else:
        return "Producto no encontrado."
    
def agregar_stock(producto: str, unidades: int) -> None:
    if producto in products:
        products[producto] += unidades
    else:
        products[producto] = unidades

def agregar_producto(producto: str, unidades: int) -> None:
    if producto not in products:
        products[producto] = unidades
    else:
        print("El producto ya existe. Use 'agregar_stock' para aumentar el stock.")

while True:
    accion = input("Ingrese 'consultar' para consultar stock, 'agregar' para agregar unidades, 'nuevo' para agregar un nuevo producto o 'salir' para terminar: ").lower()
    if accion == 'consultar':
        producto = input("Ingrese el nombre del producto a consultar: ")
        print(f"Stock de {producto}: {consultar_stock(producto)}")
    elif accion == 'agregar':
        producto = input("Ingrese el nombre del producto: ")
        unidades = int(input("Ingrese la cantidad de unidades a agregar: "))
        agregar_stock(producto, unidades)
        print(f"Stock actualizado de {producto}: {products[producto]}")
    elif accion == 'nuevo':
        producto = input("Ingrese el nombre del nuevo producto: ")
        unidades = int(input("Ingrese la cantidad de unidades: "))
        agregar_producto(producto, unidades)
        print(f"Producto {producto} agregado con stock inicial de {unidades}.")
    elif accion == 'salir':
        break
    else:
        print("Acción no reconocida. Intente nuevamente.")

print("Programa finalizado.")

# 9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.

agenda: dict[tuple[str, str], str] = {}

while True:
    acciones: set = ("agregar", "consultar", "salir")
    accion = input(f"Ingrese una acción ({', '.join(acciones)}): ").lower()
    if accion == 'agregar':
        dia = input("Ingrese el día del evento (ej. lunes): ")
        hora = input("Ingrese la hora del evento (ej. 14:00): ")
        evento = input("Ingrese el nombre del evento: ")
        agenda[(dia, hora)] = evento
        print(f"Evento '{evento}' agregado para {dia} a las {hora}.")
    elif accion == 'consultar':
        dia = input("Ingrese el día a consultar: ")
        hora = input("Ingrese la hora a consultar: ")
        clave = (dia, hora)
        if clave in agenda:
            print(f"Evento programado para {clave}: {agenda[clave]}")
        else:
            print(f"No hay eventos programados para {clave}.")
    elif accion == 'salir':
        break
    else:
        print("Acción no reconocida. Intente nuevamente.")

print("Programa finalizado.")


# 10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde:
# • Las capitales sean las claves.
# • Los países sean los valores.

mapamundi: dict[str, str] = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Colombia': 'Bogotá',
    'Perú': 'Lima'
}
capitales: dict[str, str] = {capital: pais for pais, capital in mapamundi.items()}
print(f"Nuevo diccionario con capitales como claves: {capitales}")