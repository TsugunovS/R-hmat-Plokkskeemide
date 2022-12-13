from math import * 
from random import * 
#Rühmatöö Plokkskeemide
print=input("Sisesta ikood")
a=len()
if a==11 and text.isdigit():
    print("sisestage tekst")
else:
    print("välju või vähe")














#13/12/22

r=randint(-100,100)
a=randint(-100,100)
print(f"r={r}\na={a}")
if r>0 and a>0:
    Skv=a**2
    Skr=pi*r**2
    if Skv>Skr:
        print(f"Ruudu pindala {Skv} on suurem ringi pindala {Skr}")
    elif Skr>Skv:
        print(f"Ruudu pindala {Skr} on suurem ringi pindala {Skv}")
    else:
        print("Pindalad on võrdsed. {Skr} m^2")
else:
    print(f"{a} ja {r} paevad > kui 0 olla")

print()
