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
    j_vesztett_2()

def jatekos_vesztett_teszt():
    gep = [10, 6]
    jatekos = [10, 9, 5]
    vart_eredmeny = "játékos vesztett"
    kapott_eredmeny = eredmeny(gep,jatekos)

    if kapott_eredmeny == vart_eredmeny:
        print(" \"játékos vesztett\" teszt sikeres")
    else:
        print("\"játékos vesztett\" teszt megbukott")

def j_vesztett_2():
    gep = [10, 6, 10]
    jatekos = [10, 9, 5]

    if len(gep)<len(jatekos):
        print(" \"játékos vesztett\" teszt sikeres")
    else:
        print("\"játékos vesztett\" teszt megbukott")



tesztesetek()

