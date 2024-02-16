llista = []
while True:
    num = input("Introdueix un numero ")
    if num == "final":
        break
    else:
        llista.append(int(num))
llista.sort()
print("El minim valor es ", llista[0])
print("El maxim valor es", llista [-1])
