# megoldas

# def pontokosszege(gLapok, jLapok):
#     gPontok = 0
#     jPontok = 0
#
#     for i in range(len(gLapok)):
#         gPontok += gLapok[i]
#
#     for i in range(len(jLapok)):
#         jPontok += jLapok[i]
#
#     return gPontok, jPontok

def pontokosszege2(lapok):
    pontok = 0
    for i in range(len(lapok)):
        pontok += lapok[i]

    return pontok
def eredmeny(gPontok, jPontok):

    if jPontok > 21:
        print("játékos vesztett")

    if gPontok > 21:
        print("gép vesztett")

# teszt esetek