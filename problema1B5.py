llista = []
while True:
    num = input("Introdueix un numero ")
    if num == "final":
        break
    else:
        llista.append(int(num))
        resultat = 0
        print(llista)
for i in llista:
    resultat = resultat + i
print("El resultat es ", resultat)
