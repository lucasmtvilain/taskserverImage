import rechercheMatrice
import cv2
import numpy
import neopixel
import board
import time
def afficheHeure(heure, minute):
	num_pixels = 16 * 16
	pixel_pin = board.D18
	ORDER = neopixel.GRB

	pixels = neopixel.NeoPixel(pixel_pin, num_pixels, auto_write=True, pixel_order=ORDER)

	led = faireHeure(heure, minute)
	mesLeds = rechercheMatrice.createTableauLed(16,16)
	for l in led:
            x = l[0]
            y = l[1]
            maLed = rechercheMatrice.retourneLedNumero(mesLeds, x,y)
            pixels[maLed] = (76, 65, 98)
	#pixels[rechercheMatrice.retourneLedNumero(mesLeds, 0,3)]= (76, 65, 98)
	#pixels.show()

def faireHeure(heure, minutes):
	tableauLed = []
	xdepart = 0
	tableauLed = determinateChiffre(tableauLed,xdepart, heure)
	#ajout des 2 points
	tableauLed.append([7,6])
	tableauLed.append([7,8])
	xdepart = 9
	tableauLed = determinateChiffre(tableauLed,xdepart, minutes)
	return tableauLed
def determinateChiffre(tableauLed,xdepart, chiffre):
	first = chiffre[0]
	second = chiffre[1]
	tableauLed = deternimateNumber(tableauLed,xdepart, first)
	xdepart += 3
	tableauLed = deternimateNumber(tableauLed,xdepart, second)
	return tableauLed
def deternimateNumber(tableauLed,xdepart,chiffre):
	xmax = xdepart+ 2
	if chiffre == "0":
		for x in range (xdepart, xmax+1):
			if x == xmax or x == xdepart:
				for y in range (4, 11):
					tableauLed.append([x,y])
			else :
				tableauLed.append([x, 4])
				tableauLed.append([x,10])
	elif chiffre == "1":
		xdepart+=1
		for y in range (4, 11):
			tableauLed.append([xdepart, y])
	elif chiffre == "2":
		for x in range (xdepart, xmax+1):
			tableauLed.append([x, 4])
			tableauLed.append([x, 7])
			tableauLed.append([x, 10])			
		for y in range (4, 8):
			tableauLed.append([xmax, y])
		for y in range (7, 11):
			tableauLed.append([xdepart, y])
	elif chiffre == "3":
		for x in range (xdepart, xmax+1):
			tableauLed.append([x, 4])
			tableauLed.append([x, 7])
			tableauLed.append([x, 10])			
		for y in range (4, 11):
			tableauLed.append([xmax, y])
	elif chiffre == "4":
		for x in range (xdepart, xmax+1):
			tableauLed.append([x, 7])		
		for y in range (4, 8):
			tableauLed.append([xdepart, y])
		for y in range (4, 11):
			tableauLed.append([xmax, y])
	elif chiffre == "5":
		for x in range (xdepart, xmax+1):
			tableauLed.append([x, 4])
			tableauLed.append([x, 7])
			tableauLed.append([x, 10])	
		for y in range (4, 8):
			tableauLed.append([xdepart, y])
		for y in range (7, 11):
			tableauLed.append([xmax, y])
	elif chiffre == "6":
		for x in range (xdepart, xmax+1):
			tableauLed.append([x, 4])
			tableauLed.append([x, 7])
			tableauLed.append([x, 10])	
		for y in range (4, 8):
			tableauLed.append([xdepart, y])
		for y in range (7, 11):
			tableauLed.append([xdepart, y])
			tableauLed.append([xmax, y])
	elif chiffre == "7": 
		for y in range (4,8):
			tableauLed.append([xdepart, y])
		for y in range (4,11):
			tableauLed.append([xmax, y])
		for x in range (xdepart, xmax+1):
			tableauLed.append([x, 4])	
	elif chiffre == "8":
		for x in range (xdepart, xmax+1):
			tableauLed.append([x,4])
			tableauLed.append([x,7])
			tableauLed.append([x,10])
		for y in range (4, 11):
			tableauLed.append([xdepart, y])
			tableauLed.append([xmax, y])
	elif chiffre == "9":
		for x in range (xdepart, xmax+1):
			tableauLed.append([x,4])
			tableauLed.append([x,7])
			tableauLed.append([x,10])
		for y in range (4, 8):
			tableauLed.append([xdepart, y])
		for y in range (4, 11):
			tableauLed.append([xmax, y])		
	return tableauLed

#afficheHeure("10","10")
