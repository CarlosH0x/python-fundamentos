# Programa de cálculo de custo para uma viagem
nome = input("Digite seu nome: ")
distancia = float(input("Digite a distância da viagem em km: "))
consumo_km_por_litro = float(input("Digite a consumo em km/l: "))

preco_gasolina = float(input("Digite o valor da Gasolina: "))
total_litros = distancia / consumo_km_por_litro
custos_total = total_litros * preco_gasolina

viagem_loga = distancia > 100

print(f"\n==== Resumo da Viagem de {nome.title()} ====")
print(f"Distaância total: {distancia:.2f} km")
print(f"Litros de combustível necessários: {total_litros:.2f} litros.")
print(f"Custo total estimado: {custos_total:.2f}.")
print(f"A viagem é considerada longa? {viagem_loga}\n")