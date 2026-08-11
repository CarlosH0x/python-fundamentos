print("\n===== Cálculo de Notas Escolares =====\n")

matematica = float(input("Digite sua nota final em Matemática: "))
portugues = float(input("Digite sua nota final em Potuguês: "))
geografia = float(input("Digite sua nota final em Geografia: "))
fisica = float(input("Digite sua nota final em Física: "))
biologia = float(input("Digite sua nota final em Biologia: "))
quimica = float(input("Digite sua nota final em Quimica: "))

media = (matematica + portugues + geografia + fisica + biologia + quimica) / 6

print(f"\nSua nota média foi de {media:.1f}.\n")

if media >= 6:
    print("Parabéns, você foi aprovado!")
elif media >= 4:
    print("Você não atingiu a média ideal, vai para a recuperação.")
else:
    print("Você foi reprovado!")

print("\nFIM")