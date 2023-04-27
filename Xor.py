
def codificar_xor(mensaje, clave):
    """Codifica o descodifica un mensaje en xor dado una clave.
    Args:
      mensaje: mensaje que se quiere codificar o descodificar.
      clave: clave con la que se codifica el mensaje.

    Returns:
        El mensaje codificado o descodificado.
    """
    flag = ""

    for i in range(len(mensaje)):
        flag += chr(ord(mensaje[i]) ^ ord(clave[i % len(clave)]))

    return flag


clave = "XOR"
flag = codificar_xor("+*5-=;¡.61!47=?9;;;.", clave)
print(f"El texto oculto es --> {flag}")
texto_codificado = codificar_xor(flag, clave)
print(f"volviendolo a codificar nos queda --> {texto_codificado}")
