#Programa de cálculo de massa corporal(IMC)
#Autor: Carlos Henrique
#Data: 22/07/2026

print("\n===== Cálculo de Massa Corporal IMC =====") #Início do programa

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2) #Cálculo do IMC

print(f"\nSeu IMC calculado é {imc:.2f}") #Resultado do cálculo

if imc < 18.5:
    print("Classificação: Você está abaixo do peso ideal.")
elif imc < 25:
    print("Classificação: Peso normal.")
elif imc < 30:
    print("Classificação: Sobrepeso.")
else:
    print("Classificação: Obesidade.")

print("\n=========== Fim do programa ============\n")