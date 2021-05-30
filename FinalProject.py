from PIL import Image, ImageOps
import requests
from io import BytesIO

import json

def shadow(filename):
    response = requests.get(filename)
    img = Image.open(BytesIO(response.content)).convert("L")
    image = ImageOps.colorize(img,black="white", white="black")
    return image

def main():
    print('Who is that Pokemon? ')

    with open('pokemon.json') as Pokemon:
        data = json.load(Pokemon)
        img_url=data['pokemon'][3]['img']
        response = requests.get(img_url)
        img = Image.open(BytesIO(response.content))
        img.show()
        print(img)

        #Grayscale image
        img_shadow = shadow(img_url)
        img_shadow.show()
        print(response)

if __name__== '__main__':
    main()