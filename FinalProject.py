from PIL import Image, ImageOps
import requests
from io import BytesIO

import json
import random

def play_game(name, about, img):
    INITIAL_GUESSES = 5
    list_guesses = []
    print('\nThe Pokemon name now looks like this: ',len(name)*'-')

    while True:
        result =""
        print('\nYou have ', INITIAL_GUESSES,' guesses left')
        guess = (input('Type a single letter here, then press enter: ')).upper()

        if len(guess) != 1:
            print('Please, press just one letter')
        else:
            if guess in name:
                list_guesses.append(guess)
            else:
                print('There are no '+ str(guess)+"\'s in the word")
                INITIAL_GUESSES -= 1

        for letter in name:
            if letter in list_guesses:
                result += letter   
            else:
                result += '-'
            
        #Show the progress of the game
        if result != name.upper():
            print('The Pokemon name now looks like this: '+ result)
        else:
            print('\n🥳 Congratulations, the pokemon name is:', name, '\nAbout:', about)
            img.show()
            break

        #Show when you lost the game
        if INITIAL_GUESSES == 0:
            print('Sorry, you lost. The secret word was:', name)
            break

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
    print('There is information about 251 Pokemon from the Kanto and Johto regions. Your mission will be to guess the Pokemon shown in the image. \nGotta catch \'em all!\n')
    print('🤩 Who is that Pokemon? ')
    see_image =input("Press enter to see the image ")
    if see_image != '':
        input("Just press enter to see the image ")

    with open('pokemon.json') as Pokemon:
        
        data = json.load(Pokemon)
        index = random.randint(0,len(data['pokemon'])-1)
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

        print('\n💡 Some clues about this pokemon', 
            "\nType: ", pokemon_type, 
            "\nRegion: ", region, 
            '\nQuick move: ', quick_move)
        
        #data about the pokemon
        name =data['pokemon'][index]['name']
        about = data['pokemon'][index]['about']
        
        print('name ', name)

        #Pokemon name guessing
        play_game(name.upper(), about, img)
            

if __name__== '__main__':
    main()