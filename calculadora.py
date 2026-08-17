usuario = input("Escribe tu nombre: ")

print("Registra el tiempo diario que consumes en las siguientes plataformas mencionadas")
print("puede ser en fracciones, ej.: 1.5, 2.4, etc.")
redes = float(input("Escribe tus horas en redes sociales: " ))
mensajeria = float(input("Escribe tus horas en servicios de mensajeria: " ))
streaming = float(input("Escribe tus horas en servicios de streaming: " ))
videojuegos  = float(input("Escribe tus horas en videojuegos: " ))
estudio =float(input("Escribe tus horas estudiando: " ))

total = (
    redes
    + mensajeria
    + streaming
    + videojuegos
    + estudio
)
porcentaje_dia = (total / 24) * 100

print("----- Resumen de tiempo -----")
print({usuario})
print(f"Tiempo total invertido: {total} horas")
print(f"Porcentaje dentro del día: {porcentaje_dia}%")