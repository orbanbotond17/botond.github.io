import random

gondoltSzam = random.randint(1, 100)
tipp = 0

tipp = int(input("Gondoltam egy számra, tippeld meg:"))
tipp = int(input("Próbáld újra:"))

while tipp != gondoltSzam:
    if tipp < gondoltSzam:
        print("A gondolt szam NAGYOBB, mint a tipped")
    elif tipp > gondoltSzam:
        print("A gondolt szam KISEBB, mint a tipped")
tipp = int(input("Kérem az újabb tippet"))

print("Kitaláltad a gondolt számot!")  