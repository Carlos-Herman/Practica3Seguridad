# cifrado vigenere
# funciones
def codificar_vigenere(descifrar, clave, alfabeto, direccion):
    clave_len = len(clave)
    descifrar_len = len(descifrar)
    alfabeto_len = len(alfabeto)
    flag = ""
    for i in range(descifrar_len):
        clave_char = clave[i % clave_len]
        descifrar_char = descifrar[i % descifrar_len]
        if descifrar_char not in alfabeto:
            flag += descifrar_char
            continue

        clave_pos = alfabeto.index(clave_char)
        descifrar_pos = alfabeto.index(descifrar_char)
        flag_pos = (descifrar_pos - clave_pos*direccion) % alfabeto_len
        flag_char = alfabeto[flag_pos]
        flag += flag_char
    return flag
# la función de descodificar puede usar la anterior, cambiando el valor de dirección,
# para que el desplazamiento de las letras sea en sentido opuesto
def descodificarVigenere(descifrar, clave, alfabeto, direccion):
    return codificar_vigenere(descifrar, clave, alfabeto, -direccion)

# programa principal
alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
textoCifrado = "QqmiaiiiYmisqmwmxijs"
clave = "Vigenere"
flag = codificar_vigenere(textoCifrado, clave, alfabeto, 1)
print(f"El texto oculto es --> {flag}")
texto_codificado = descodificarVigenere(flag, clave, alfabeto, 1)
print(f"volviendolo a codificar nos queda --> {texto_codificado}")
