llista = []
while True:
    num = input("Introdueix un numero ")
    llista.append(num)
    if num == "final":
        llista.pop(-1)
        break
print(llista)
