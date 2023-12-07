magassag = float(input("Add meg a magasságod(cm):"))

testsúly = float(input("Add meg a testsúly(kg):"))

magassagMeterben = magassag / 100

BMI = testsúly / (magassagMeterben * magassagMeterben)

print("Az ön testtömegindexe (BMI) :",BMI)

if BMI < 18.5:
    print("Ön alultáplált")
    print(" O")
    print(")I(")
    print("I I")
elif BMI >= 18.5 and BMI < 24.9:
    print("Ön testsúlya ideális")
    print("O")
    print("(I)")
    print("I I")    
elif BMI >= 24.9 and BMI < 29.9:
    print("Ön túlsúlyos")
    print("O")
    print("( )")
    print("I I")
elif BMI >= 29.9 and BMI < 34.9: 
    print("Ön elhízott")
    print(" O")
    print("(   )")
    print("I   I")
elif BMI >= 34.9 and BMI < 39.9:
    print("Ön súlyosan elhízott")
    print("  O ")
    print("(     )")
    print("I     I")
else:
    print("Ön morbidan elhízott")
    print("     O")
    print("(*       *)")
    print("I         I")
