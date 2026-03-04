saldo = 1000

operaciones = int(input("¿Cuántas operaciones desea realizar? "))

for i in range(operaciones):

    print("\n--- MENÚ ---")
    print("1 → Consultar saldo")
    print("2 → Retirar dinero")
    print("3 → Depositar dinero")

    opcion = int(input("Elija una opción: "))

    if opcion == 1:
        print("Su saldo actual es:", saldo)

    elif opcion == 2:
        monto = float(input("Ingrese el monto a retirar: "))

        while monto < 0:
            monto = float(input("Monto inválido. Ingrese un monto positivo: "))

        if monto > saldo:
            print("Fondos insuficientes")
        else:
            saldo -= monto
            print("Retiro exitoso. Nuevo saldo:", saldo)

    elif opcion == 3:
        monto = float(input("Ingrese el monto a depositar: "))

        while monto < 0:
            monto = float(input("Monto inválido. Ingrese un monto positivo: "))

        saldo += monto
        print("Depósito exitoso. Nuevo saldo:", saldo)

    else:
        print("Opción inválida")

print("\nGracias por usar el cajero automático")