from random import randrange
znak = input("x nebo o?")
pozice = 0
if znak == "x":
    pc = "o"
elif znak == "o":
    pc = "x"
else:
    pc = "x"
print("Tvůj znak je ", znak, ". Počítač má znak ", pc)
pole = 20*"-"
def tah():
    global b
    pozice = int(input("zadej pozicu:  "))
    if pole[pozice] == znak or pole[pozice] == pc:
        print("Tady uz je obsazeno")
        b = pole
        tah()
    else:
        b = pole[:pozice] + znak + pole[pozice + 1:]
def ptah():
    global c
    global d
    c = randrange(0, len(pole))
    if pole[c] == znak or pole[c] == pc:
        ptah()
    else:
        d = pole[:c] + pc + pole[c + 1:]

def vyhodnot():
    global q
    if (3 * znak in pole) == True:
        print("Gratuluji, vyhravas!")
        q = False
    elif (3 * pc in pole) == True:
        print("maybe next time bro")
        q = False
    else:
        q = True
while True:
    tah()
    print("Stare pole je ", pole)
    pole = b
    vyhodnot()
    print("Snove pole je ", pole)
    ptah()
    vyhodnot()
    print("Stare pole je ", d)
    if q == False:
        break
