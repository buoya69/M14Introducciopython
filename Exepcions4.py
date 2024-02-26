llista_elements = [10, 20, 30, 40, 50]
try:
    index = int(input("Introdueix un índex per accedir a la llista: "))
    element = llista_elements
    print(f"L'element a l'índex es ", element)
except ValueError:
    print("Error: L'índex proporcionat no existeix a la llista.")
