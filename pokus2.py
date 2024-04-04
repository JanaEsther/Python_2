
import random

try:
    cislo_ruleta = random.randint(0, 36)
    cislo_sazka = int(input("Na které číslo sázíš? "))
    if not 0 <= cislo_sazka <= 36:
        raise ValueError
        if cislo_sazka == cislo_ruleta:
            print("Gratuluji, vyhráváš!")

except ValueError:
    print("Je třeba zadat číslo v rozsahu 0 až 36!")
except TypeError:
    print("Je třeba zadat číslo.")









