import base64

def codificador_64(cadena):
    text_bytes = cadena.encode('ascii')
    encoded_bytes = base64.b64encode(text_bytes)
    encoded_text = encoded_bytes.decode('ascii')
    return encoded_text

def descodificador_64(cadena):
    encoded_bytes = cadena.encode('ascii')
    text_bytes = base64.b64decode(encoded_bytes)
    text = text_bytes.decode('ascii')
    return text

descifrar = "MjAyM19TZWd1cmlkYWRJbmZvcm1hdGljYUJhc2U2NA=="
flag = descodificador_64(descifrar)
print(f"El texto oculto es --> {flag}")
texto_codificado = codificador_64(flag)
print(f"volviendolo a codificar nos queda --> {texto_codificado}")
