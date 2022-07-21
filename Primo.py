def es_primo(numero):
    list = [2, 3, 5, 7, 9]

    for i in list:

        if numero % i == 0 and numero != i:
            return False

    else:
        return True


def run():
    numero = int(input("Escriba un numero: "))

    if es_primo(numero):
        print("Es primo")

    else:
        print("No es primo")


if __name__ == '__main__':
    run()