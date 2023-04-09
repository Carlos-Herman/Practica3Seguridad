def codificar_vigenere(descifrar , clave ,alfabeto):
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
        flag_pos = (descifrar_pos + clave_pos) % alfabeto_len
        flag_char = alfabeto[flag_pos]
        flag += flag_char
    return flag

def descodificar_vigenere(descifrar , clave ,alfabeto):
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
        flag_pos = (descifrar_pos - clave_pos) % alfabeto_len
        flag_char = alfabeto[flag_pos]
        flag += flag_char
    return flag



alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
descodificar = "QqmiaiiiYmisqmwmxijs"
clave = "Vigenere"
flag = descodificar_vigenere(descodificar, clave, alfabeto)
print(f"El texto oculto es --> {flag}")
texto_codificado = codificar_vigenere(flag, clave, alfabeto)
print(f"volviendolo a codificar nos queda --> {texto_codificado}")
