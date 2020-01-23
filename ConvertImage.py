import cv2
import numpy
import rechercheMatrice
import neopixel
import board
import time


def convert_file(ImageUrl):


    # récupération de l'image sur le serveur
    img = cv2.imread(
        ImageUrl,
        cv2.IMREAD_UNCHANGED)
    #cv2.imshow("Resized image", img)

    # Reduction de la taille de l'image
    scale_percent = 60  # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)

    while (width >= 16 or height >= 16):
        width = int(width * scale_percent / 100)
        height = int(height * scale_percent / 100)

    matrixNeo = rechercheMatrice.createTableauLed(16, 16)

    matrixNeo.reverse()

    num_pixels = 16*16
    pixel_pin = board.D18
    ORDER = neopixel.GRB

    pixels = neopixel.NeoPixel(pixel_pin, num_pixels,brightness=0.2,auto_write=False,pixel_order=ORDER )

    # dim = (16, 16)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    # Conversion image en tableau à 3 entrée
    matrixRGB = numpy.empty((height, width, 3), dtype=numpy.uint8)

    print(resized)
    test = numpy.asarray(resized)
    test = numpy.flip(test,0)
    mawidth = width
    for i in range(0,height):
        test[i] = numpy.flip(test[i],0)
        for j in range(0,width):
            pixels[rechercheMatrice.retourneLedNumero(matrixNeo,j,i)] = (test[i][j][0], test[i][j][1], test[i][j][2])
        pixels.show()
        time.sleep(2)


    time.sleep(10)

    #cv2.imshow("resultat en 16x16", matrixRGB)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    print('image uploadé !')


#convert_file('C:/Users/Utilisateur/Documents/Cours/5_annee/rasberry/serverUpload/template/test.png')
