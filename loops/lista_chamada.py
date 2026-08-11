# Programa de lista de chamada
import time # Biblioteca que controla o tempo
estudantes = ["Carlos", "Isabela", "Julio", "Marcela", "Eduardo"] # Definindo uma lista de nomes
total_estudantes = 0

# Iniciando o loop 'for' para percorrer a lista
for nome in estudantes:
    time.sleep(1) # Cada chamada de nome vai ter 1 segundo de intervalo
    # Mensagem que será repetida para cada item na lista
    print(f"Bem-vindo(a), {nome}! Sua presença foi registrada.")

    # Atualizando o contador
    total_estudantes += 1

# Menssagem final após o loop
print(f"\nAula iniciada. Total de {total_estudantes} estudantes presentes.")