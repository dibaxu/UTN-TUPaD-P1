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