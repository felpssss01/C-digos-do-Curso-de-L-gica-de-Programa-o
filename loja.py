import os
os.system("cls")

produto = str(input("Digite o nome do produto: "))
preco_uni = float(input("Digite o preço unitário do produto: "))
quantidade = int(input("Digite a quantidade de produto que o senhor deseja comprar: "))
desconto = float(input("Digite o percentual de desconto: "))

subtotal = preco_uni * quantidade
valor_desconto = subtotal * desconto / 100
total = subtotal - valor_desconto

print("\n --- RESUMO DA COMPRA ---")
print(f"produto: {produto}")
print(f"preço unitário: R$ {preco_uni: .2f} ")
print(f"quantidade comprada: {quantidade}")
print(f"desconto: {desconto}%")
print(f"total: R$ {total: .2f}")
