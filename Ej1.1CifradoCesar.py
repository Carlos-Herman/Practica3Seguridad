"""
Este cifrado, que lleva el nombre de Julio C´esar, es uno de los tipos de cifrados m´as antiguos y se
basa en el cifrado monoalfab´etico de desplazamiento, tambi´en es com´un verle llamado “ROT-N”,
donde N hace referencia al desplazamiento que se va a aplicar.
"""
import string

def codificarCesar(text, offset):
    return decodificarCesar(text, -offset)


def decodificarCesar(text, offset):
    decodedText = []
    lowerCase = string.ascii_lowercase
    upperCase = string.ascii_uppercase

    for letter in text:
        for element in range(len(lowerCase)-1):
            newLetter = ""
            if letter == lowerCase[element]:
                newLetter = lowerCase[(element + offset) % len(lowerCase)]

            elif letter == upperCase[element]:
                newLetter = upperCase[(element + offset) % len(upperCase)]

            decodedText.append(newLetter)

    return decodedText


# ASCII de mayusculas: de 65 a 90 // de minúsculas: de 97 a 122


textDecode = "MyaolcxuxChzilguncwuWymul"
textCode = "SeguridadInormaticaCesar"

for i in range(25):
    #sol = decodificarCesar(text, i)
    sol = codificarCesar(textCode, i)
    print("".join(sol), end = "")
    print()


