import random
import string

print("Here You can Generate a Password:  ")

def fuc():
    length = int(input("Enter the Length of Password: "))
    print(length)

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    special_char = string.punctuation
    digit = string.digits

    combine = lowercase + uppercase +special_char +digit

    password = random.sample(combine , length)

    x = " ".join(password)
    print(x)
    fuc()

fuc()    