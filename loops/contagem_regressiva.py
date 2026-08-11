# Programa de Contagem Regressiva com 'while'
import time # Biblioteca 'time' que será usada para controlar o tempo da contagem

print("--- Iniciador de Foguete ---\n")

# Variável com valor negativo para garantir que o primeiro loop seja executado pelo menos uma vez, já que a condição será True (-1 é menor que 0)
segundos = - 1

# Primeiro loop while com validação de entrada
while segundos < 0:
    segundos = int(input("Digite a partir de quantos segundos o foguete deve partir: "))

    if segundos < 0:
        print("Erro: O tempo não pode ser negativo. Tente novamente.")

# Segundo loop while para a repetição da contagem
while segundos > 0:
    time.sleep(1) # Com isso cada contagem demora 1 segundo
    print(f"Lançamento em: {segundos}...")
    segundos -= 1 # Isso atualiza a variável para evitar loop infinito

print("\nFoguete lançado!")