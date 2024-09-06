# 1 - Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

def check_fibonacci_number(num):
    fib_sequence = fibonacci_sequence(num)
    
    if num in fib_sequence:
        print(f"O numero {num} pertence a sequencia de Fibonacci.")
    else:
        print(f"O numero {num} NAO pertence a sequencia de Fibonacci.")

# Exemplo de uso:
numero = int(input("Informe um número: "))
check_fibonacci_number(numero)
