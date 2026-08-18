
sin_pago = 0       # Menores de 3 años
precio_menor = 30  # De 3 a 17 años
precio_adulto = 45 # Mayores de 18 años

# porcentajes de descuento
descuento_adulto_mayor = 0.12
descuento_profesor = 0.10
descuento_estudiante = 0.10

total_general = 0

num_visitantes = int(input("¿Cuántos visitantes van a pagar boleto? "))

for i in range(num_visitantes):
    print(f"\n----- Visitante {i + 1} -----")
    edad = int(input("Edad del visitante: "))

    if edad < 3:
        print("Menor de 3 años, sin cargo")
        continue

    mayor_edad = input("¿Es mayor de edad? (si/no): ").lower()

    if edad >= 18 and mayor_edad == "no":
        print("Error: la edad no coincide con la respuesta. Intente de nuevo.")
        break

    if edad < 18 and mayor_edad == "si":
        print("Error: la edad no coincide con la respuesta. Intente de nuevo.")
        break

    tipo_visitante = input("Tipo de visitante (adulto mayor/profesor/estudiante/normal): ").lower()

    if edad <= 17:
        precio_base = precio_menor
    else:
        precio_base = precio_adulto

    descuento = 0
    if tipo_visitante == "adulto mayor":
        descuento = precio_base * descuento_adulto_mayor
    elif tipo_visitante == "profesor":
        descuento = precio_base * descuento_profesor
    elif tipo_visitante == "estudiante":
        descuento = precio_base * descuento_estudiante

    precio_final = precio_base - descuento
    total_general += precio_final

    print(f"Precio base:    ${precio_base:.2f}")
    print(f"Descuento:     -${descuento:.2f}")
    print(f"Total a pagar:  ${precio_final:.2f}")

print("\n----- Resumen de la cuenta -----")
print(f"Visitantes: {num_visitantes}")
print(f"Total a pagar: ${total_general:.2f}")

