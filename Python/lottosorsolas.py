#Lottó számok listájának létrehozása

import random

LottGomb = []

for i in range (0, 91):
    LottGomb.append(i)
    
print(LottGomb)
print("****************************************************************************************************")
random.shuffle(LottGomb)
print(LottGomb)
print("****************************************************************************************************")