# megoldas
def pontokosszege2(lapok: [int]):
    pontok: int = 0
    for i in range(len(lapok)):
        pontok += lapok[i]

    return pontok


def eredmeny(gLapok: [int], jLapok: [int]):
    jPontok: int = pontokosszege2(jLapok)
    gPontok: int = pontokosszege2(gLapok)
    vegeredmeny = ""
    if jPontok and gPontok > 21:
        vegeredmeny = "mindenki vesztett"
    elif gPontok > 21:
        vegeredmeny = "gép vesztett"
    elif jPontok > 21:
        vegeredmeny = "játékos vesztett"

    return vegeredmeny

# teszt esetek
def tesztesetek():
    jatekos_vesztett_teszt()

def jatekos_vesztett_teszt():
    jatekos = [10, 9, 3]
    gep = [10, 6]
    vart_eredmeny = "játékos vesztett"
    kapott_eredmeny = eredmeny(gep,jatekos)

    if kapott_eredmeny == vart_eredmeny:
        print("a teszt sikeres")
    else:
        print("a teszt megbukott")

tesztesetek()