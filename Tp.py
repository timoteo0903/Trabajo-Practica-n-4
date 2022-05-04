
print("""----------- HOLA SOY TU SALE-MANAGER -----------""")
print("Vas a pasar a cargar los datos de tus dias en los cuales realizaste alguna venta. ")
continuar = "si"
venta_x_dia= [ ]
while continuar == "si" and continuar != "no":    
    dia = int(input("De que dia quiere cargar las ventas? "))
    while dia not in range (0,32):
        dia = int(input("Inserte un dia entre 1 y 31. "))
    print("Vamos con la primera venta del dia: ")
    respuesta = 1
    contD = 0
    contC = 0 
    contP = 0
    while respuesta != 0:
        ventas = [ ]
        Tipo_empaque = str(input("Ingrese el tipo de empaque: 1-Individual ; 2-Caja "))
        while Tipo_empaque != "1" and Tipo_empaque != "2":
            Tipo_empaque = str(input("ERROR!. Ingrese el tipo de empaque: 1-Individual ; 2-Caja "))
        if Tipo_empaque =="1":
            Sabor = str(input("Ingrese el sabor del cubanito: 'D'- Dulce de Leche ; 'C'-Chocolate ; 'P'- Pasta de Mani")).upper()
            while Sabor != "D" and Sabor != "C" and Sabor != "P":
                Sabor = str(input("ERROR!. Ingrese el sabor del cubanito: 'D'- Dulce de Leche ; 'C'-Chocolate ; 'P'- Pasta de Mani")).upper()
        else:
            Sabor = str(input("Ingrese el sabor del cubanito: 'D'- Dulce de Leche ; 'C'-Chocolate ; 'P'- Pasta de Mani; 'M'- Mezcla ")).upper()
            while Sabor != "D" and Sabor != "C" and Sabor != "P" and Sabor != "M":
                Sabor = str(input("ERROR!. Ingrese el sabor del cubanito: 'D'- Dulce de Leche ; 'C'-Chocolate ; 'P'- Pasta de Mani;'M'- Mezcla ")).upper()
        Cantidad = int(input("Ingrese la cantidad vendida: "))
        if Tipo_empaque == "1":
            if Sabor == "D":
                contD += Cantidad
            elif Sabor == "C":
                contC +=  Cantidad
            elif Sabor == "P":
                contP +=  Cantidad
        else:
            if Sabor == "D":
                contD +=  6 * Cantidad
            elif Sabor == "C":
                contC +=  6 * Cantidad
            elif Sabor == "P":
                contP +=  6 * Cantidad
            elif Sabor == "M": 
                contD +=  2 * Cantidad 
                contC +=  2 * Cantidad
                contP +=  2 * Cantidad 
        total = contC + contD + contP
        porcentajeD = (contD / total) * 100
        porcentajeC = (contC / total) * 100
        porcentajeP = (contP / total) * 100
        recaudacion = total * 10
        ventas.append(dia)
        ventas.append(porcentajeC)
        ventas.append(porcentajeD)
        ventas.append(porcentajeP)
        ventas.append(recaudacion)
        respuesta = int(input("Si desea agregar otra venta presione: 1. Si desea pasar al dia siguiente presione: 0."))
        venta_x_dia.append(ventas)
    continuar = str(input("Desea agregar las ventas de otro dia? (si/no)")).lower()
    while continuar != "si" and continuar != "no":
        continuar = str(input("Desea agregar las ventas de otro dia? (si/no)")).lower()
    
mayor_rec = venta_x_dia [0][4]
rec_tot = 0
for n in venta_x_dia:
    for x in n:
        t = 0 
        while t <= len(ventas):
            t += 1
            if t == 0:
                dia = x 
            if t == 4:
                rec_dia = x 
    rec_tot = rec_dia + rec_tot
    if len(venta_x_dia) == 1: 
        print("El dia que mas recaudo fue el dia ", dia)
    else: 
        if rec_dia > mayor_rec:
            mayor_rec = rec_dia 
            mejor_dia = dia
print("El dia que mas recaudo fue el dia ", str(mejor_dia) , " Y recaudo: ", str(mayor_rec))
print("La recaudacion total del mes fue: ", str(rec_tot))



    
