from math import * 
from random import * 
#14/12/22
try:
    vanus=int(input("Kui vana sa oled? "))
    if vanus>18:
        print("Kas te annate vanamatele loa oma Tahvelit vaadata")
        o=(input("Jah või ei. "))
        if o.lower()=="jah": #upper() будет делать все буквы большими
            print({o})
            print("See on ligipääs teie vanematele")
            print("Tahvel on kinni.")
        elif o.upper()=="EI":
             print("Sissepääs puudub.")
             print("Tahvel on kinni.")
    if vanus<18:
        print("Juurdepääs vanematele on automaatselt antud.")
except:
    print("Tahvel on kinni.")
print()
print()








try:
    päev=int(input("Mis päev ja mitu tundi täna on ?"))
    if päev==1:
        n="Esmaspäev"
        n="6tundi"
    elif päev==2:
        n="teisipäev"
        n="8 tundi"
    elif päev==3:
        n="Kolmapäev"
        n="6 tundi"
    elif päev==4:
        n="Neljapäev"
        n="? tundi"
    elif päev==5:
        n="Reede"
        n="7 tundi"
    elif päev==6:
        n="Laupäev"
        n="0 tundi"
    elif päev==7:
        n="Pühapäev"
        n="0 tundi"
    else:
        n="Vile number!"
    print(n)
except:
    print("!!!!!!!!")



#Rühmatöö Plokkskeemide
print=input("Sisesta ikood")
a=len()
if a==11 and text.isdigit():
    print("sisestage tekst")
else:
    print("välju või vähe")
    print


#Задача на оценеи
try:
    hinne=int(input("mis on täna tulemus"))
except:
    print("!!!!!?")
if hinne==5:
    print("väga hea!")
elif hinne==4:
    print("Hea!")
elif hinne==3:
    print("Rahuldav")
elif hinne==2 or hinne==1:
    print("halvasti!")
else:
    print("viga!")














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
