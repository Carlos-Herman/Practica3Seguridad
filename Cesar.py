
def codificar_cesar(mensaje, desplazamiento):
    """Codifica o descodifica un mensaje en Vingere dado un alfabeto y una clave.
    Args:
      mensaje: mensaje que se quiere codificar.
      desplazamiento: numero de desplazamientos que se quiere realizar, si se quiere descodificar,
       se debe introducir el numero negativo.

    Returns:
        El mensaje codificado o descodificado.

    """
    flag = ""
    alfabeto = "abcdefghijklmnopqrstuvwxyz"

    for letra in mensaje:
        flag_letra=""
        if letra.lower() in alfabeto:
            flag_letra = alfabeto[(alfabeto.index(letra.lower()) + desplazamiento) % len(alfabeto)]

        if letra.isupper():
            flag += flag_letra.upper()
        else:
            flag += flag_letra

    return flag


for i in range(26):
    flag = codificarCesar("MyaolcxuxChzilguncwuWymul", i)
    print(f"Desplazamiento: {i} - Mensaje--> {flag}")

"""
Para descodificar el mensaje, se debe introducir el numero negativo en el desplazamiento.
Hemos encontrado que el ROT correcto es el ROT-6 y que la flag es: SeguridadInformaticaCesar
Probamos el descodificador con estos valores
"""

texto_codificado = codificarCesar("SeguridadInformaticaCesar", -6)
print(f"volviendolo a codificar nos queda --> {texto_codificado}")