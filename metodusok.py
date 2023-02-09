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
    if jPontok > 21 and gPontok > 21:
        vegeredmeny = "mindenkinek több, mint 21"
    elif gPontok > 21:
        vegeredmeny = "több mint 21: gép vesztett"
    elif jPontok > 21:
        vegeredmeny = "több mint 21: játékos vesztett"
    elif jPontok < 21 and gPontok < 21 and len(jLapok) == len(gLapok):
        vegeredmeny = "kevesebb mint 21 mindkettő, de ugyanannyi lapszám"
    elif jPontok == gPontok:
        vegeredmeny = "döntetlen"
    elif gPontok == 21:
        vegeredmeny = "pont21: gép nyert"
    elif jPontok == 21:
        vegeredmeny = "pont21: játékos nyert"
    elif jPontok == 19 and len(jLapok) > len(gLapok):
        vegeredmeny = "19 pont, de több lap teszt: játékos nyert"
    elif gPontok == 19 and len(gLapok) > len(jLapok):
        vegeredmeny = "19 pont, de több lap teszt: gép nyert"
    elif jPontok == 19 and len(jLapok) < len(gLapok):
        vegeredmeny = "19 pont, de kevesebb lap teszt: játékos nyert"
    elif gPontok == 19 and len(gLapok) < len(jLapok):
        vegeredmeny = "19 pont, de kevesebb lap teszt: gép nyert"
    elif jPontok == 19 and len(jLapok) > len(gLapok):
        vegeredmeny = "19pont, több lap teszt: játékos vesztett"
    elif jPontok == 19 and len(jLapok) < len(gLapok):
        vegeredmeny = "19pont, kevesebb lap teszt: játékos vesztett"
    elif gPontok == 19 and len(gLapok) > len(jLapok):
        vegeredmeny = "19pont, több lap teszt: gép vesztett"
    elif gPontok == 19 and len(gLapok) < len(jLapok):
        vegeredmeny = "19pont, kevesebb lap teszt: gép vesztett"
    elif gPontok > jPontok:
        vegeredmeny = "kisebb mint 21: gép nyert"
    elif jPontok > gPontok:
        vegeredmeny = "kisebb mint 21: játékos nyert"




    return vegeredmeny


# teszt esetek
def tesztesetek():
    jatekos_tobb21()
    jatekos_veszt_pont19tobblap()
    jatekos_veszt_pont19kevesebblap()
    gep_tobb21()
    gep_veszt_pont19tobblap()
    gep_veszt_pont19kevesebblap()
    dontelen_21pont()
    dontetlen_megegyezolapszam()
    dontetlen_tobbmint21()
    jatekospont21()
    geppont21()
    jatekospont19_tobblap()
    geppont19_tobblap()
    jatekospont19_kevesebblap()
    geppont19_kevesebblap()

def jatekos_tobb21():
    gep = [10, 6]
    jatekos = [10, 10, 3]
    vart_eredmeny = "több mint 21: játékos vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if kapott_eredmeny == vart_eredmeny:
        print("több mint 21 játékos vesztett teszt: sikeres")
    else:
        print("több mint 21 játékos vesztett teszt: megbukott")

def jatekos_veszt_pont19tobblap():
    gep = [10, 5]
    jatekos = [10, 5, 4]
    vart_eredmeny = "19pont, több lap teszt: játékos vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("19pont, de több lap teszt játékos veszt: sikeres")
    else:
        print("19 pont, de több lap teszt játékos veszt: megbukott")



def jatekos_veszt_pont19kevesebblap():
    gep = [10, 5, 4]
    jatekos = [10, 9]
    vart_eredmeny = "19pont, kevesebb lap teszt: játékos vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("19pont, de kevesebb lap teszt játékos veszt: sikeres")
    else:
        print("19 pont, de kevesebb lap teszt játékos veszt: megbukott")


# •Ha lapok összege > 21, akkor az vesztett•
# •Aki közelebb van a 21-hez, az nyert•
# •Döntetlen esetén az nyer, akinek kevesebb a lapja

def gep_tobb21():
    gep = [10, 10, 2]
    jatekos = [10, 6]
    vart_eredmeny = "több mint 21: gép vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if kapott_eredmeny == vart_eredmeny:
        print("több mint 21 gép vesztett teszt: sikeres")
    else:
        print("több mint 21 gép vesztett teszt: megbukott")


def gep_veszt_pont19tobblap():
    gep = [10, 5, 4]
    jatekos = [10, 4]
    vart_eredmeny = "19pont, több lap teszt: gép vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("19pont, de több lap teszt gép veszt: sikeres")
    else:
        print("19 pont, de több lap teszt gép veszt: megbukott")

def gep_veszt_pont19kevesebblap():
    gep = [10, 9]
    jatekos = [10, 5]
    vart_eredmeny = "19pont, kevesebb lap teszt: gép vesztett"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("19pont, de kevesebb lap teszt gép veszt: sikeres")
    else:
        print("19 pont, de kevesebb lap teszt gép veszt: megbukott")

def dontelen_21pont():
    gep = [10, 10, 1]
    jatekos = [10, 5, 6]
    vart_eredmeny = "döntetlen"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("döntetlen, pont 21pont teszt: sikeres")
    else:
        print("döntetlen, pont 21pont teszt: megbukott")

def dontetlen_tobbmint21():
    gep = [10, 10, 5]
    jatekos = [10, 10, 3]
    vart_eredmeny = "mindenkinek több, mint 21"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("mindenkinek több, mint 21 teszt: sikeres")
    else:
        print("mindenkinek több, mint 21 teszt: megbukott")
def dontetlen_megegyezolapszam():
    jatekos = [10, 5]
    gep = [8, 7]
    vart_eredmeny = "kevesebb mint 21 mindkettő, de ugyanannyi lapszám"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("kevesebb mint 21 mindkettő, de ugyanannyi lapszám teszt: sikeres")
    else:
        print("kevesebb mint 21 mindkettő, de ugyanannyi lapszám teszt: megbukott")

def jatekospont21():
    gep = [10, 10]
    jatekos = [10, 10, 1]
    vart_eredmeny = "pont21: játékos nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("pont21 játékos nyer teszt: sikeres")
    else:
        print("pont21 játékos nyer teszt: megbukott")

def geppont21():
    gep = [10, 10, 1]
    jatekos = [10, 10]
    vart_eredmeny = "pont21: gép nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("pont21 gép nyer teszt: sikeres")
    else:
        print("pont21 gép nyer teszt: megbukott")

def jatekospont19_tobblap():
    gep = [10, 1]
    jatekos = [10, 5, 4]
    vart_eredmeny = "19 pont, de több lap teszt: játékos nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("19 pont, de több lap teszt játékos nyer: sikeres")
    else:
        print("19 pont, de több lap teszt játékos nyer: megbukott")

def geppont19_tobblap():
    gep = [10, 1, 8]
    jatekos = [10, 8]
    vart_eredmeny = "19 pont, de több lap teszt: gép nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("19 pont, de több lap teszt gép nyer: sikeres")
    else:
        print("19 pont, de több lap teszt gép nyer: megbukott")

def jatekospont19_kevesebblap():
    gep = [10, 4, 3]
    jatekos = [10, 9]
    vart_eredmeny = "19 pont, de kevesebb lap teszt: játékos nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("19 pont, de kevesebb lap teszt játékos nyer: sikeres")
    else:
        print("19 pont, de kevesebb lap teszt játékos nyer: megbukott")

def geppont19_kevesebblap():
    gep = [10, 9]
    jatekos = [10, 3, 4]
    vart_eredmeny = "19 pont, de kevesebb lap teszt: gép nyert"
    kapott_eredmeny = eredmeny(gep, jatekos)

    if vart_eredmeny == kapott_eredmeny:
        print("19 pont, de kevesebb lap teszt gép nyer: sikeres")
    else:
        print("19 pont, de kevesebb lap teszt gép nyer: megbukott")


tesztesetek()
