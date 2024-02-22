import random

def daus_x():
    numero_daus = int(input("Quants daus has de llençar?: "))
    cares = int(input("Quants cares té el dau?: "))
    for i in range(numero_daus):
        print(random.randint(1, cares))
