def createTableauLed(width, height):
	#Déterminer la led en fonction de x et y
	nbPas = 16

	liste = []

	for i in range (0, height):
		liste.append([0] * nbPas)

	cpt = 0
	for i in range (0, height):
		if cpt == 64:
			print(cpt)
			cpt -= 1
			print(cpt)
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

monTableauLed = createTableauLed(16,16)

print(monTableauLed)




