import os
os.system("cls") #limpa a tela do terminal

nome = input("Qual é o seu nome estudante? ")

n1 = float(input("Digte a nota do seu primeiro bimestre: "))

n2 = float(input("Digite a nota do segundo bimestre: "))

n3= float(input("Digite a nota do terceiro bimestre: "))

n4 = float(input("Digite a nota do quarto bimestre: "))

media = (n1 + n2 + n3 + n4) / 4

print(nome)
print(n1)
print(n2)
print(n3)
print(n4)
print(media)

print("\n--- Resultado ---")
print(f"Estudante: {nome}")
print(f"Média: {media: 2f}")