from Crypto.Cipher import AES
import binascii

def codificar_aesCBC(mensaje, clave, iv):
    """Codifica un mensaje en AES modo CBC
    Args:
      mensaje: mensaje que se quiere codificar.
      clave: clave con la que se codifica el mensaje.
      iv: vector de inicialización.

    Returns:
        El mensaje codificado.

    """
    cipher = AES.new(clave, AES.MODE_CBC, iv)
    cifrado = cipher.encrypt(mensaje.encode("utf-8"))

    return cifrado.hex()


def descodificar_aesCBC(mensaje, clave, iv):
    """Codifica un mensaje en AES modo CBC
    Args:
      mensaje: mensaje que se quiere codificar.
      clave: clave con la que se codifica el mensaje.
      iv: vector de inicialización.

    Returns:
        El mensaje descodificado.

    """
    cipher = AES.new(clave, AES.MODE_CBC, iv)
    flag = cipher.decrypt(mensaje)

    return flag.decode("utf-8")


descodificar_hex = binascii.unhexlify("9bc43d7ec1aa11f64302287b17be9f7b")
clave_b = b"SeguridadInforma"
iv_b = b"SeguridadInforma"
flag = descodificar_aesCBC(descodificar_hex, clave_b, iv_b)
print(f"El texto oculto es --> {flag}")
texto_codificado = codificar_aesCBC(flag, clave_b, iv_b)
print(f"volviendolo a codificar nos queda --> {texto_codificado}")
