
def codificar_vigenere(mensaje, clave, alfabeto, direccion):
    """Codifica o descodifica un mensaje en Vingere dado un alfabeto y una clave.
    Args:
      mensaje: mensaje que se quiere codificar.
      clave: clave con la que se codifica el mensaje.
      alfabeto: alfabeto de la tabla de Vigenere.
      direccion: 1 para codificar, 0 para descodificar.

    Returns:
        El mensaje codificado o descodificado.

    """
    flag = ""

    for i in range(len(mensaje)):
        clave_char = clave[i % len(clave)]
        mensaje_char = mensaje[i % len(mensaje)]

        if mensaje_char not in alfabeto:
            flag += mensaje_char
            continue

        if direccion == 1:
            flag_pos = (alfabeto.index(mensaje_char) - alfabeto.index(clave_char)) % len(alfabeto)
        else:
            flag_pos = (alfabeto.index(mensaje_char) + alfabeto.index(clave_char)) % len(alfabeto)
        flag += alfabeto[flag_pos]

    return flag


alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
clave = "Vigenere"
flag = codificar_vigenere("QqmiaiiiYmisqmwmxijs", clave, alfabeto, 1)
print(f"El texto oculto es --> {flag}")
texto_codificado = codificar_vigenere(flag, clave, alfabeto, 0)
print(f"volviendolo a codificar nos queda --> {texto_codificado}")