# Un analista financiero lleva un registro del precio del dólar día a día, y desea saber cuál fue la mayor
# de las alzas en el precio diario a lo largo de ese período.
# Escriba un programa que pida al usuario ingresar el número n de días, y luego el precio del dólar para cada uno de los n días.
# El programa debe entregar como salida cuál fue la mayor de las alzas de un día para el otro.	
# Si en ningún día el precio subió, la salida debe decir: No hubo alzas.

Alza = []
vDolar = []

nDias = int(input("Favor ingrese el numero de dias: "))
print("Favor ingrese el precio del dolar del:")
for i in range(1, nDias + 1):
    Dolar = int(input(f"Dia {i}: "))
    vDolar.append(Dolar)

for i in range(nDias - 1):
    Alza_1 = vDolar[i + 1] - vDolar[i]
    Alza.append(Alza_1)

maxAlza = max(Alza)

print(f"La mayor alza fue de {maxAlza}.")
