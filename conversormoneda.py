print("\n----- Conversor de moneda -----")

# tipo de cambio
tipo_cambio_usd = 18.50
tipo_cambio_eur = 21.00

cantidad_mxn = float(input("Cantidad en MXN: "))

# conversiones
usd = cantidad_mxn / tipo_cambio_usd
eur = cantidad_mxn / tipo_cambio_eur

print(f"\n${cantidad_mxn} MXN equivalen a:")
print(f"USD: ${usd}")
print(f"EUR: €{eur}")

