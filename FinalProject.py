from PIL import Image, ImageOps
import requests
from io import BytesIO

import json
import random

def shadow(filename):
    response = requests.get(filename)
    img = Image.open(BytesIO(response.content)).convert("L")
    image = ImageOps.colorize(img,black="white", white="black")
    return image

def movements(quick_move):
    value =[]
    for i in range(len(quick_move)):
            value.append(quick_move[i]['name'])
    return value

def main():
    print('👋 Welcome to Pokemon data')
    print('Below is information for 251 Pokemon from the Kanto and Johto regions. Your mission will be to guess the Pokemon shown in the image. \nGotta catch \'em all!\n')
    print('🤩 Who is that Pokemon? ')
    input("Press enter to see the image ")

    index = random.randint(0,250)

    with open('pokemon.json') as Pokemon:
        data = json.load(Pokemon)
        img_url=data['pokemon'][index]['img']
        response = requests.get(img_url)
        img = Image.open(BytesIO(response.content))

        #Grayscale image
        img_shadow = shadow(img_url)
        img_shadow.show()

        #Clues
        pokemon_type = data['pokemon'][index]['type']
        region = data['pokemon'][index]['generation']['name']
        quick_move = movements(data['pokemon'][index]['quick-move'])
        
        name =data['pokemon'][index]['name']
        print('\n💡 Some clues about this pokemon')
        print("Type: ", pokemon_type)
        print("Region: ", region)
        print('Quick move: ', quick_move)
        print('name ', name)

        #Attempts
        guess = len(name)*'-'
        print('The Pokemon name now looks like this: ',guess)
       

        img.show()

if __name__== '__main__':
    main()