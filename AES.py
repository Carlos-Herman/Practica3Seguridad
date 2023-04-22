from Crypto.Cipher import AES
import binascii


def codificar_aesCBC(mensaje, clave, iv):
    cipher = AES.new(clave, AES.MODE_CBC, iv)
    cifrado = cipher.encrypt(mensaje.encode('utf-8'))
    return cifrado.hex()


def descodificar_aesCBC(mensaje, clave, iv):
    cipher = AES.new(clave, AES.MODE_CBC, iv)
    cifrado = cipher.decrypt(mensaje)
    return cifrado.decode('utf-8')


descodificar = binascii.unhexlify('9bc43d7ec1aa11f64302287b17be9f7b')
clave = b'SeguridadInforma'
iv = b'SeguridadInforma'
flag = descodificar_aesCBC(descodificar, clave, iv)
print(f"El texto oculto es --> {flag}")
texto_codificado = codificar_aesCBC(flag, clave, iv)
print(f"volviendolo a codificar nos queda --> {texto_codificado}")
