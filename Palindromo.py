def palindromo(frase):
    frase = frase.replace(' ', '').lower()

    if frase[::] == frase[::-1]:
        return True

    else:
        return False


def run():
    frase = input('Escribe una palabre o frase: ')
    es_palindromo = palindromo(frase)

    if es_palindromo == True:
        print("Es palindromo")

    else:
        print("No es palindromo")


if __name__ == '__main__':
    run()