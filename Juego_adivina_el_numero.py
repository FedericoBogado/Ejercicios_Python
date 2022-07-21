import random


def ciclo(num_random, num_elegido):
    vidas = 4

    while num_random != num_elegido and vidas > 0:

        if num_elegido < 0 or num_elegido > 100:
            num_elegido = int(input("¡¡¡DIJE DEL 0 AL 100!!! "))

        elif num_elegido < num_random:
            num_elegido = int(input("Ingrese un numero mas alto: "))
            vidas -= 1

        else:
            num_elegido = int(input("Ingrese un numero mas bajo: "))
            vidas -= 1

    if vidas < 1:
        print("¡Perdiste!")
        print("El numero era:", num_random)
        
    else:
        print("¡Ganaste!")


def run():
    num_random = random.randint(0, 100)
    num_elegido = int(input("Ingrese un numero del 0 al 100: "))
    ciclo(num_random, num_elegido)


if __name__ == '__main__':
    run()