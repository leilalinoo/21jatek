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
    elif gPontok > jPontok:
        vegeredmeny = "kisebb mint 21: gép nyert"
    elif jPontok > gPontok:
        vegeredmeny = "kisebb mint 21: játékos nyert"
    elif jPontok == gPontok:
        vegeredmeny = "döntetlen"

    return vegeredmeny


# teszt esetek
def tesztesetek():
    jatekos_vesztett_teszt()
    j_vesztett_2()
    j_veszt_3()
    gep_vesztett_teszt()
    gep_vesztett2()
    gep_vesztett3()
    kisebb21gepnyer()
    dontelen()

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
    jatekos = [10, 6]
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


def kisebb21gepnyer():
    gep = [10, 8]
    jatekos = [10, 1]
    vart_eredmeny = "kisebb mint 21: gép nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("kisebb mint 21: gép nyert")
    else:
        print("kisebb mint 21: játékos nyert")


def dontelen():
    gep = [10, 1, 9]
    jatekos = [10, 10]
    vart_eredmeny = "döntetlen"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        if len(gep) < len(jatekos):
            print("döntetlen teszt: gép nyert")
        else:
            print("döntetlen teszt: jatékos nyert")


tesztesetek()
