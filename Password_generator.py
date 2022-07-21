import random
import string


def password_generator():
    #MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    #MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    #NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    #CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    
    characters = string.ascii_lowercase + string.digits + string.punctuation + string.ascii_uppercase

    password = []

    for i in range(15):
        random_charac = random.choice(characters)
        password.append(random_charac)

    password = "".join(password)

    return password


def run():
    password = password_generator()
    print("Your new password is:", password)


if __name__ == "__main__":
    run()