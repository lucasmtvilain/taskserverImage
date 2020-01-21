def createTableauLed(width, heigth):
    #nbPas = 16

    liste = []

    for i in range (0, heigth):
        liste.append([0] * width)

    cpt = 0
    for i in range (0, heigth):
        for j in range (0,width):
            liste[i][j] = cpt
            cpt+= 1

    for i in range (1, len(liste)):
        if i%2 != 0:
            liste[i].reverse()
            i+=1

    liste.reverse()
    return liste

def retourneLedNumero(liste, x,y):
	return liste[y][x]

width = 0
heigth=0

monTableauLed = createTableauLed(width, heigth)

(retourneLedNumero(monTableauLed, 11, 14))