import board
import neopixel
import ConvertImage
from flask import Flask, request

pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
pixels[0] = (10, 0, 0)

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return 'index !'

@app.route('/LedApi', methods = ['GET', 'POST'])
def booksFunction():
   if request.method == 'GET':
       return get_Time()
   #elif request.method == 'POST':
    #   title = request.args.get('title', '')
    #   author = request.args.get('author', '')
    #   genre = request.args.get('genre', '')
    #   return makeANewBook(title, author, genre)

def get_Time():
    return 'heure'




if __name__ == '__main__':
    app.run()
