# 2- Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.

def contar_letra_a(string):
    # Converte a string para minúsculas para contar 'a' e 'A' de forma case insensitive
    string_lower = string.lower()
    
    # Conta quantas vezes a letra 'a' aparece
    contagem = string_lower.count('a')
    
    # Verifica se a letra 'a' aparece
    if contagem > 0:
        print(f"A letra 'a' aparece {contagem} vezes na string.")
    else:
        print("A letra 'a' nao aparece na string.")

# Exemplo de uso:
texto = input("Digite uma string: ")
contar_letra_a(texto)
