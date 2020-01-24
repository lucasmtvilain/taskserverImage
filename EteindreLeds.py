import neopixel
import board
import rechercheMatrice
def eteindreLeds():
	num_pixels = 16 * 16
	pixel_pin = board.D18
	ORDER = neopixel.GRB

	pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER)
	mesLeds = rechercheMatrice.createTableauLed(16,16)
	for l in (0,len(mesLeds)):
		for i in range (0,len(mesLeds[l])):
			print(rechercheMatrice.retourneLedNumero(mesLeds, i,l))
			pixels[rechercheMatrice.retourneLedNumero(mesLeds, i,l)] = (0, 0, 0)
		pixels.show()
