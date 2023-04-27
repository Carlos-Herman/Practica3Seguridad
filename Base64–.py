import base64

def codificador_64(mensaje):
    """Codifica en base65 dado un alfabeto y una clave.
    Args:
        mensaje: mensaje que se quiere codificar.

    Returns:
        El mensaje codificado.

    """
    flag_bytes = mensaje.encode("ascii")
    cifrado_bytes = base64.b64encode(flag_bytes)
    cifrado = cifrado_bytes.decode("ascii")

    return cifrado

def descodificador_64(mensaje):
    """Descodifica en base65 dado un alfabeto y una clave.
    Args:
        mensaje: mensaje que se quiere descodificar.

    Returns:
        El mensaje descodificado.

    """
    mensaje_bytes = mensaje.encode("ascii")
    flag_bytes = base64.b64decode(mensaje_bytes)
    flag = flag_bytes.decode("ascii")

    return flag


flag = descodificador_64("MjAyM19TZWd1cmlkYWRJbmZvcm1hdGljYUJhc2U2NA==")
print(f"El texto oculto es --> {flag}")
texto_codificado = codificador_64(flag)
print(f"volviendolo a codificar nos queda --> {texto_codificado}")
