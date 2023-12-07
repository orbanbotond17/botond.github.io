def bmi_kalkulator(testsuly, testmagassag):
    """Számolja ki a BMI-t adott testsúly és testmagasság alapján."""
    bmi = testsuly / (testmagassag ** 2)
    return bmi

def ertekelo(bmi):
    """Értékelje a BMI-t és adja vissza az eredményt."""
    if bmi < 18.5:
        return "Alacsony testsúly"
    elif 18.5 <= bmi < 24.9:
        return "Normál testsúly"
    elif 25 <= bmi < 29.9:
        return "Túlsúly"
    elif 30 <= bmi < 34.9:
        return "Első fokú elhízás"
    elif 35 <= bmi < 39.9:
        return "Másodfokú elhízás"
    else:
        return "Súlyos, harmadfokú elhízás"

# Felhasználótól kérjük be a testsúlyt és a testmagasságot
testsuly = float(input("Kérem, adja meg a testsúlyát kilogrammban: "))
testmagassag = float(input("Kérem, adja meg a testmagasságát méterben: "))

# Számoljuk ki a BMI-t
bmi = bmi_kalkulator(testsuly, testmagassag)

# Értékeljük a BMI-t
ertekles = ertekelo(bmi)

# Eredmény kiírása
print(f"A BMI értéke: {bmi:.2f}")
print(f"Értékelés: {ertekles}")
