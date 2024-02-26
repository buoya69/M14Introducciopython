try:
    valor1 = float(input("Introdueix el primer valor: "))
    valor2 = float(input("Introdueix el segon valor: "))

    suma = valor1 + valor2
    print("La suma es: ", suma)

except:
    print("Error: Introdueix dos valors numèrics vàlids.")
