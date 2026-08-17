print("\n----- Calificación final -----")

parcial1 = float(input("Parcial 1 (30%): "))
parcial2 = float(input("Parcial 2 (30%): "))
parcial3 = float(input("Parcial 3 (40%): "))

calificacion_final = (
    (parcial1 * 0.30)
    + (parcial2 * 0.30)
    + (parcial3 * 0.40)
)

if calificacion_final >= 60:
    print(f"Tu calificación final es de {calificacion_final}. ¡Has aprobado!")

else:
    print(f"Tu calificación final es de {calificacion_final}. No has aprobado. ")