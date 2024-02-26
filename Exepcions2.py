entrada = input("Introdueix un numero: ")
try:
    numero = int(entrada)
    print("El nombre enter introduït és: ", numero)
except:
    print("Error: Si us plau, introdueix un nombre vàlid.")
