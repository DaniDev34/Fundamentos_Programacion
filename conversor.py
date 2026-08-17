print("\n----- Conversor de tiempo -----")

while True:

    print("\n¿Qué quieres hacer?")
    print("1. Convertir horas a minutos")
    print("2. Convertir minutos a horas")
    print("3. Convertir días a minutos")
    print("4. Convertir minutos a días, horas y minutos")
    print("0. Salir")

    opcion = input("\nSelecciona una opción: ")

    # Horas a minutos
    if opcion == "1":

        horas = float(input("\nIngresa la cantidad de horas: "))

        minutos = horas * 60

        print(f"\n{horas} horas equivalen a {minutos} minutos")


    # Minutos a horas
    elif opcion == "2":

        minutos = float(input("\nIngresa la cantidad de minutos: "))

        horas = minutos / 60

        print(f"\n{minutos} minutos equivalen a {horas} horas")


    # Días a minutos
    elif opcion == "3":

        dias = float(input("\nIngresa la cantidad de días: "))

        minutos = dias * 24 * 60

        print(f"\n{dias} días equivalen a {minutos} minutos")


    # Minutos → días, horas y minutos
    elif opcion == "4":

        minutos = int(input("\nIngresa la cantidad total de minutos: "))

        # Día en minutos: 1440 minutos
        dias = minutos // 1440

        # sobrante después de sacar los días
        minutos_restantes = minutos % 1440

        # Convertir los minutos restantes en horas
        horas = minutos_restantes // 60

        # minutos sobrantes después de sacar las horas
        minutos_finales = minutos_restantes % 60

        print(f"\n{minutos} minutos equivalen a:")
        print(f"{dias} días, {horas} horas y {minutos_finales} minutos")


    # para salir
    elif opcion == "0":

        print("\n Cerrando programa")
        break


    # Opción incorrecta
    else:

        print("\nOpción no válida. Prueba de nuevo.")
