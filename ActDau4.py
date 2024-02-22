import random

def dau_x():
    tirades = int(input("Quantes tirades vols fer? "))
    cares = int(input("Quantes cares te el dau? "))
    for i in range (1,tirades+1):
        resultat = random.randint(1, cares)
        print(resultat)
dau_x()
