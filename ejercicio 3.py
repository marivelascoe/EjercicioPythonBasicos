alimentos = [["A", "B", "C"], [270, 340, 390]]
con = 0
opc = 0
moneda = 0

bandera = True
while bandera:
    print("* * * * * * * * Maquina de Alimentos * * * * * * * *")
    print(" 0 - Productos A.......................$ 270 ")
    print(" 1 - Productos B.......................$ 340 ")
    print(" 2 - Productos C.......................$ 390 ")
    print("Escoja qué producto le gustaría")
    for i in alimentos[0]:
        print(f"\t{con}. {i}")
        con += 1
    try:
        opc = int(input("\n"))
        if 0 <= opc <= len(alimentos[0]) - 1: bandera = False
        else: raise 
    except:
        print("Opcion incorrecta, por favor ingrese una opcion valida.")
        bandera = True
    finally:
        con = 0

precio = alimentos[1][opc]

print ("Recuerde esta maquina solo recibe modedas de 10, 50, o 100")
while moneda < precio:
    valor_moneda = int(input("Ingrese el valor de la moneda: "))
    if valor_moneda in [10, 50, 100]:
        moneda += valor_moneda
    else:
        print("El valor de la moneda no es válido. Inténtelo de nuevo.")

cambio = moneda - precio

while cambio > 0:
    if cambio >= 50:
        print("Su cambio es: $50")
        cambio -= 50
    elif cambio >= 10:
        print("Su cambio es: $10")
        cambio -= 10
