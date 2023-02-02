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
    j_veszt_3()
    gep_vesztett_teszt()
    gep_vesztett2()
    gep_vesztett3()
    kisebb21()

def jatekos_vesztett_teszt():
    gep = [10, 6]
    jatekos = [10, 10, 3]
    vart_eredmeny = "játékos vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if kapott_eredmeny == vart_eredmeny:
        print("1. \"játékos vesztett\" teszt sikeres")
    else:
        print("1. \"játékos vesztett\" teszt megbukott")


def j_vesztett_2():
    gep = [10, 10, 1]
    jatekos = [10, 9]
    vart_eredmeny = "játékos vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if kapott_eredmeny == vart_eredmeny:
        print("2. \"játékos vesztett\" teszt sikeres")
    else:
        print("2. \"játékos vesztett\" teszt megbukott")


def j_veszt_3():
    gep = [10, 10]
    jatekos = [10, 10, 1]
    vart_eredmeny = "játékos vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if kapott_eredmeny == vart_eredmeny:
        print("3. \"játékos vesztett\" teszt sikeres")
    else:
        print("3. \"játékos vesztett\" teszt megbukott")


# •Ha lapok összege > 21, akkor az vesztett•
# •Aki közelebb van a 21-hez, az nyert•
# •Döntetlen esetén az nyer, akinek kevesebb a lapja

def gep_vesztett_teszt():
    gep = [10, 10, 2]
    jatekos = [10, 1]
    vart_eredmeny = "gép vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if kapott_eredmeny == vart_eredmeny:
        print("1. \"gép vesztett\" teszt sikeres")
    else:
        print("1. \"gép vesztett\" teszt megbukott")


def gep_vesztett2():
    gep = [10, 9]
    jatekos = [10, 10, 1]
    vart_eredmeny = "gép vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if kapott_eredmeny == vart_eredmeny:
        print("2. \"gép vesztett\" teszt sikeres")
    else:
        print("2. \"gép vesztett\" teszt megbukott")


def gep_vesztett3():
    gep = [10, 10]
    jatekos = [10, 10, 1]
    vart_eredmeny = "gép vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if kapott_eredmeny == vart_eredmeny:
        print("3. \"gép vesztett\" teszt sikeres")
    else:
        print("3. \"gép vesztett\" teszt megbukott")


def kisebb21():
    gep = [10, 8]
    jatekos = [10, 1]
    geppont = 0
    jatekospont = 0

    for i in range(len(gep)):
        geppont += gep[i]

    for i in range(len(jatekos)):
        geppont += jatekos[i]

    if geppont < 21 and jatekospont < 21:
        if geppont > jatekospont:
            print("kisebb mint 21 teszt: gep nyert")
        elif jatekospont > geppont:
            print("kisebb mint 21 teszt: gep nyert")


tesztesetek()
