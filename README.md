# cajero-automtico
#definicion de variables
saldo_actual= 1000
#solicitar al usuario el numero de operaciones a realizar
opciones = int(input("¿Cuántas operaciones desea realizar? "))   
#ciclo para realizar operaciones
for i in range(opciones):
    #menu de opciones
    print("\nMenu de opciones:")
    print("1. Retirar dinero")
    print("2. Consignar dinero")
    print("3. Consultar saldo")
    print("4. Salir")       
    #solicitar al usuario la opcion a realizar 
    opcion = int(input("Elija una opcion: "))
    #condicionales para cada opcion
    if opcion == 1:
        valor = float((input("Ingrese el valor a retirar: ")))
        #validar que el valor sea positivo
        while valor < 0:
            valor = float(input("valor invalido, porfavor ingrese un valor positivo: "))
#validar que el monto a retirar no supere el saldo disponible
        if valor >  saldo_actual:
            print("Fondos insuficientes")
        else:
            saldo_actual -= valor                                   
            print("Retiro exitoso. Nuevo saldo:", saldo_actual)
    if opcion == 2:
        valor = float(input("Ingrese el valor a consignar: "))
        #validar que el valor sea positivo
        while valor < 0:
            valor = float(input("valor invalido, porfavor ingrese un valor positivo: "))
        saldo_actual += valor
        print("Consignacion exitosa. Nuevo saldo:", saldo_actual)
    if opcion == 3:                                                      
        print("Su saldo actual es:", saldo_actual           )
    if opcion == 4:
        print("Gracias por usar el cajero automatico")
