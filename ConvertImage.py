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
    scale_percent = 1.1  # percent of original size
    width = int(img.shape[1] / scale_percent)
    height = int(img.shape[0] / scale_percent)

    while (width >= 16 or height >= 16):
        width = int(width / scale_percent)
        height = int(height / scale_percent)

    matrixNeo = rechercheMatrice.createTableauLed(height, width)

    num_pixels = height*width
    pixel_pin = board.D18
    ORDER = neopixel.GRB

    pixels = neopixel.NeoPixel(pixel_pin, num_pixels,brightness=0.2,auto_write=False,pixel_order=ORDER )

    # dim = (16, 16)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    # Conversion image en tableau à 3 entrée
    matrixRGB = numpy.empty((height, width, 3), dtype=numpy.uint8)

    for i in range(height):
        for j in range(width):
            matrixRGB[i, j, 0] = resized[i, j, 0]
            matrixRGB[i, j, 1] = resized[i, j, 1]
            matrixRGB[i, j, 2] = resized[i, j, 2]

    for i in range(height):
        for j in range(width):
            pixels[rechercheMatrice.retourneLedNumero(matrixNeo,i,j)] = (matrixRGB[i, j, 0], matrixRGB[i, j, 1], matrixRGB[i, j, 2])



    time.sleep(10)

    #cv2.imshow("resultat en 16x16", matrixRGB)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    print('image uploadé !')


#convert_file('C:/Users/Utilisateur/Documents/Cours/5_annee/rasberry/serverUpload/template/test.png')