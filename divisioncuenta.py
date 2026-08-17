taco = 10
quesadilla = 25
pozole= 70
agua = 30

cantidad_tacos = int(input("¿Cuántos tacos consumieron? "))
cantidad_quesadillas = int(input("¿Cuántas quesadillas consumieron? "))
cantidad_pozole = int(input("¿Cuántos pozoles consumieron? "))
cantidad_agua = int(input("¿Cuántas aguas consumieron? "))

subtotal = (
    (taco * cantidad_tacos)
    + (quesadilla * cantidad_quesadillas)
    + (pozole * cantidad_pozole)
    + (agua * cantidad_agua)
)

propina = float(input("¿Deseas agregar propina? "))
personas = int(input("¿Entre cuántas personas se dividirá la cuenta? "))

monto_propina = subtotal * (propina / 100)
total = subtotal + monto_propina
por_persona = total / personas

print(f"\n ----- Resumen de la cuenta -----")
print(f"\nTacos: {cantidad_tacos}")
print(f"\nQuesadillas: {cantidad_quesadillas}")
print(f"\nPozole: {cantidad_pozole}")
print(f"\nAguas: {cantidad_agua}")
print(f"\nCuenta: ${subtotal}")
print(f"Propina: ${monto_propina}")
print(f"Total a pagar: ${total}")
print(f"Total por persona: ${por_persona}")