# Programa que simula o cálculo de orçamento para um freelancer
print("===== Calculador de Projeto Freelancer =====\n")

nome_projeto = input("Digite o nome do projeto: ")
horas_estimadas = int(input("Digite a quantidade de horas estimada para o projeto: "))
valor_hora = float(input("Digite o valor da hora do projeto: "))

# Cálculo do projeto
custos_fixos = float(input("Digite os custos fixos do projeto: ")) # Ex: Software, internet, liz, etc
receita_total = horas_estimadas * valor_hora
lucro_liquido = receita_total - custos_fixos

produto_valioso = lucro_liquido > 500.00

# Saída de dados formatada
print(f"\n===== Resumo do Projeto {nome_projeto.title()} =====\n")
print(f"Receita Bruta: R$ {receita_total:.2f}")
print(f"Custos Fixos: R$ {custos_fixos:.2f}")
print(f"Lucro Liquido: R$ {lucro_liquido:.2f}")
print(f"Produto Validoso: {produto_valioso}")
