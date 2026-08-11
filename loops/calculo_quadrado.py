# Programa que calcula o quadrado dos números de 1 a 5
import time
print("Calculando os quadrados dos números de 1 a 5\n")

# Iniciando o loop 'for' com a função 'range'
for numero in range(1, 6):
    time.sleep(1) #Faz o código repetir a cada 1 segundo
    resultado = numero ** 2
    print(f"O número atual é {numero} e o seu quadrado é {resultado}")

# Finalização do progama
print("\nCálculos concluídos com sucesso!")