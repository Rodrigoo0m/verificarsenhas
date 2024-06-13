def verificarsenhas(senha):
    tem_letras_maisculas = False
    tem_letras_minusculas = False
    tem_numeros = False
    tem_caracters_especiais = False

    if len(senha) < 8:
        return "Senha fraca: A senha deve ter pelo menos 8 caracteres."

    for char in senha:
        if char.isupper():
            tem_letras_maisculas = True
        elif char.islower():
            tem_letras_minusculas = True
        elif char.isdigit():
            tem_numeros = True
        else:
            tem_caracters_especiais = True

    if (tem_letras_maisculas and tem_letras_minusculas and tem_numeros and tem_caracters_especiais):
        return "Senha forte: A senha atende os requisitos Minimos."
    else:
        return "Senha Fraca: A senha deve ter pelo menos os requisitos Minimos."

senha = input("Insira uma senha: ")

resultado = verificarsenhas(senha)
print(resultado)
