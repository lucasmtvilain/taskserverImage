import neopixel
import board
import rechercheMatrice
def eteindreLeds():
	num_pixels = 16 * 16
	pixel_pin = board.D18
	ORDER = neopixel.GRB

	pixels = neopixel.NeoPixel(pixel_pin, 254, brightness=0.2, auto_write=False, pixel_order=ORDER)
	mesLeds = rechercheMatrice.createTableauLed(16,16)
	print("je suis la")
	for j in range (0, 16):
		for i in range (0,16):
			pixels[rechercheMatrice.retourneLedNumero(mesLeds, i,j)] = (0, 0, 0)
		pixels.show()