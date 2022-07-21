import random


def run():

    while True:
        randon = random.randrange(0, 3)
        pc = ""
        jugador = int(input('Eleji tu jugada \n \n[1] Piedra \n[2] Papel \n[3] Tijera \n\n'))
        
        if jugador == 1:
            eleccion = "piedra"

        elif jugador == 2:
            eleccion = "papel"

        elif jugador == 3:
            eleccion = "tijera"

        print('\nElegiste: ', eleccion)
            
        if randon == 0:
            pc = "piedra"

        elif randon == 1:
            pc = "papel"

        elif randon == 2:
            pc = "tijera"

        print('\nLa máquina eligió: ', pc)
        
        if pc == eleccion:
            print('\n ¡Empate!')

        elif pc == "piedra" and eleccion == "papel":
            print('\n¡Ganaste!')

        elif pc == "papel" and eleccion == "tijera":
            print('\n¡Ganaste!')

        elif pc == "tijera" and eleccion == "piedra":
            print('\n¡Ganaste!')

        elif pc == "tijera" and eleccion == "papel":
            print('\n¡Perdiste!')

        elif pc == "piedra" and eleccion == "tijera":
            print('\n¡Perdiste!')
            
        elif pc == "papel" and eleccion == "piedra":
            print('\n¡Perdiste!')
            
        play_again = input('\n¿Querés volver a jugar? s/n: ')
        print('')
        
        if play_again.lower() != 's':
            break


if __name__ == "__main__":
    run()