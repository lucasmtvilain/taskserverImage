import os.path
# construct an absolute path to the directory this file is located in
HERE = os.path.dirname(os.path.abspath(__file__))
import cv2

# on recupère l'image
img = cv2.imread('C:/Users/Utilisateur/Documents/Cours/5_annee/rasberry/neopixel/template/drapeau.png',cv2.IMREAD_UNCHANGED)
cv2.imshow("Resized image", img)
# variable de retour MATRICE avec les pixels
k = []
#dimension de l'image convertis en 16 par 16

scale_percent = 220 # percent of original size
width = int(img.shape[1] * 100 /scale_percent )
height = int(img.shape[0] * 100 / scale_percent)
dim = (width, height)
#noouvel image en 16 par 16
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
# recuperation du nombre de colonne en 16 par 16
dimensions = resized.shape
rows = dimensions[0]
cols = dimensions[1]



for i in range(rows):
    for j in range(cols):
        k.append(img[i,j])


for i in range(len(k)):
    print(k[i])



