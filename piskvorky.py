from random import randrange
znak=input("x nebo o?")
pozice=0
if znak=="x":
    pc="o"
elif znak=="o":
    pc="x"
else: pc="x"
print("Tvůj znak je ",znak,". Počítač má znak ",pc)
pole=20*"-"
def tah():
    global b
    pozice=int(input("zadej pozicu:  "))
    if pole[pozice]==znak or pole[pozice]==pc:
        print("Tady uz je obsazeno")
        b=pole
        tah()
    else:
        b=pole[:pozice]+znak+pole[pozice+1:]
def ptah():
    global c
    c=randrange(0,len(pole)+1)
        if pole[c]==znak or pole[c]==pc:
            ptah()
        else:
            b=pole[:c]+pc+pole[c+1:]

while True:
    tah()
    print("Stare pole je ",pole)
    pole=b
    print("Snove pole je ",pole)
