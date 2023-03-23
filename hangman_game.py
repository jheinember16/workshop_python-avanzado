import os
import random

def welcome():
    print("Adivina LOS DEPORTES OLIMPICOS")
    print("   ▄████████    ▄█    █▄     ▄██████▄     ▄████████  ▄████████    ▄████████ ████████▄   ▄██████▄")
    print("  ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███ ███   ▀███ ███    ███")
    print("  ███    ███   ███    ███   ███    ███   ███    ███ ███    █▀    ███    ███ ███    ███ ███    ███")
    print("  ███    ███  ▄███▄▄▄▄███▄▄ ███    ███  ▄███▄▄▄▄██▀ ███          ███    ███ ███    ███ ███    ███")
    print("▀███████████ ▀▀███▀▀▀▀███▀  ███    ███ ▀▀███████▀   ███        ▀███████████ ███    ███ ███    ███")
    print("  ███    ███   ███    ███   ███    ███ ▀███████████ ███    █▄    ███    ███ ███    ███ ███    ███")
    print("  ███    ███   ███    ███   ███    ███   ███    ███ ███    ███   ███    ███ ███   ▄███ ███    ███")
    print("  ███    █▀    ███    █▀     ▀██████▀    ███    ███ ████████▀    ███    █▀  ████████▀   ▀██████▀")          

def printGame():
    die0 = '''
           '''
    die1 = '''
        _____________
      /             /|
     /____________ / |
    |             | /
    |_____________|/

          '''
    die2 = '''
          ╔
          ║
          ║
          ║
          ║
          ║
          ║
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

            '''
    die3 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║
          ║
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die4 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die5 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die6 = '''
          ╔═════╦  
          ║
          ║
          ║
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die7 = '''
          ╔═════╦  
          ║
          ║
          ║    ─┼─
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die8 = '''
          ╔═════╦  
          ║
          ║
          ║   ┌─┼─┐
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die9 = '''
          ╔═════╦  
          ║
          ║     @
          ║   ┌─┼─┐
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die10 = '''
          ╔═════╦  
          ║     │
          ║     @       ¡AHORCADO!
          ║   ┌─┼─┐
          ║     │
          ║    / '''+chr(92)+'''
          ║   d   b
        __║__________
      /   ║         /|
     /____________ / |
    |             | /
    |_____________|/

'''
    die11 = '''
          ╔═════╦  
          ║
          ║     
          ║
          ║              ¡GANASTE!
          ║
          ║                  
        __║__________        @
      /   ║         /|     └─┼─┘  
     /____________ / |       │
    |             | /       / '''+chr(92)+'''
    |_____________|/       d   b

'''
    deaths = {0: die0, 1: die1, 2: die2, 3: die3, 4: die4, 5: die5, 6: die6, 7: die7, 8: die8, 9: die9, 10: die10, 11: die11}
    return deaths

def read_word():
    word_li = []
    with open('./bancopalabras/palabras.txt', 'r', encoding='utf-8') as data_words:
        word = random.choice([word.strip().upper() for word in data_words])
    for letter in word:
        if letter == 'Á':
            letter = 'A'
        elif letter == 'É':
            letter = 'E'
        elif letter == 'Í':
            letter = 'I'
        elif letter == 'Ó':
            letter = 'O'
        elif letter == 'Ú':
            letter = 'U'
        word_li.append(letter)
    return ''.join(word_li)

def new_word(word, dict_word, discovered, deaths, letters):
    word = read_word()
    dict_word = {i[0] : i[1] for i in enumerate(word)}
    discovered = ['- ' for i in range(len(dict_word))]
    deaths = 0
    letters = ['A','B','C','D','E','F','G','H',
               'I','J','K','L','M','N','Ñ','O',
               'P','Q','R','S','T','U','V','W',
               'X','Y','Z']
    return word, dict_word, discovered, deaths, letters

def compare_letter(letter, dict_word, discovered, fail):
    for l in range(len(dict_word)):
        if dict_word.get(l) == letter:
            discovered[l] = letter + ' '
            fail = False
    return discovered, fail

def refresh(hangman_deaths,deaths,letters):
    os.system('clear')
    welcome()
    print('Total Letras disponibles: '+"  ".join(letters))
    print(hangman_deaths.get(deaths))

def gameManual():
    print("""
            Manual del Juego ----------> 
            - La maquina piensa en una palabra y tu objetivo es tratar de descrubrir dicha palabra
               adivinando las letras que la componen.
            - Tienes un limite de 10 INTENTOS
            - Empieza ingresando una letra que creas que pueda contener la palabra !! 
            
            <<  Buena Suerte , Empecemos a Jugar !!! >>
          """)

def runGame():
    hangman_deaths = printGame()
    word = ''
    dict_word = {}
    discovered = []
    deaths = 0
    letters = []
    non_letter = 0
    word, dict_word, discovered, deaths, letters = new_word(word, dict_word, discovered, deaths, letters)
    while True:
        refresh(hangman_deaths,deaths,letters)
        if non_letter == 1:
            print('Debes ingresar una de las letras disponibles')
            non_letter = 0
        try:
            letter = input('''¡Adivina la palabra!     '''+ ''.join(discovered) +'''
            Ingresa una letra: ''').upper()
            letters[letters.index(letter)] = ''
        except ValueError:
            non_letter = 1
        fail = True
        discovered,fail = compare_letter(letter, dict_word, discovered, fail)
        if fail == True:
            deaths += 1
            if deaths == 10:
                refresh(hangman_deaths,deaths,letters)
                print('¡Perdiste! La palabra era ' + word)
                again = input('¿Quieres jugar otra vez? (1-Si 0-No):  ')
                if again == '1':
                    word, dict_word, discovered, deaths, letters = new_word(word, dict_word, discovered, deaths, letters)
                    continue
                else:
                    print('Gracias por jugar :)')
                    break
        if ''.join(discovered).replace(' ','') == word:
            refresh(hangman_deaths,11,letters)
            print('Tuviste ', deaths, ' erorres      '+ ''.join(discovered))
            again = input('¿Quieres jugar otra vez? (1-Si 0-No):  ')
            if again == '1':
                word, dict_word, discovered, deaths, letters = new_word(word, dict_word, discovered, deaths,letters)
                continue
            else:
                print('Gracias por jugar :)')
                break

def chooseOption():
    principal = """
            1. Empezar Juego
            2. Manual del Juego
            3. Salir
            Digite una opcion: 
           """
    opcionEscogida = int(input(principal))
    if opcionEscogida >= 4:
        print("Ingrese un valor valido")
        chooseOption()
    if opcionEscogida <= 0 or opcionEscogida >= 4:
        exit()
    if opcionEscogida == 1:
        runGame()
    elif opcionEscogida == 2:
        gameManual()
        chooseOption()
    

def main():
    while True:
        chooseOption()

main()
