import daus
def mostrar_menu():
    print("""
1.-Llençar un dau de 6 cares.
2.-Llençar més d'un dau de 6 cares.
3.-Llençar un dau de cares definides per usuari.
4.-Llençar més d'un dau de cares definides per usuari.
5.-Sortir. 
    """)
while True:
    mostrar_menu()
    opcio = input("Introdueix opcio: ")
    if opcio == "5":
        break
    elif opcio == "1":
        daus.dau_6()
    elif opcio == "2":
        daus.daus_6()
    elif opcio == "3":
        daus.dau_x()
    elif opcio == "4":
        daus.daus_x()
