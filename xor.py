
def codificar_xor(texto, clave):
    texto_codificado = ""
    for i in range(len(texto)):
        texto_codificado += chr(ord(texto[i]) ^ ord(clave[i % len(clave)]))
    return texto_codificado

def descodificar_xor(texto, clave):
    codificar_xor(texto, clave)

descodificar = "+*5-=;¡.61!47=?9;;;."
clave = "XOR"
flag = descodificar_xor(descodificar, clave)
print(f"El texto oculto es --> {flag}")
texto_codificado = codificar_xor(flag, clave)
print(f"volviendolo a codificar nos queda --> {texto_codificado}")
