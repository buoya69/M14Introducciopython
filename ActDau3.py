import random

def daus_6():
    tirades = int(input("Quantes tirades vols fer? "))
    for i in range (1,tirades+1):
        resultat = random.randint(1, 6)
        print(resultat)
daus_6()
