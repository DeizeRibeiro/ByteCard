from model import Compra, Cartao

compra_farmacia = Compra()
compra_restaurante = Compra()
compra_supermercado = Compra()

print(compra_farmacia)
print(compra_restaurante)
print(compra_supermercado)
print()

visa = Cartao("4234 5678 9012 3456", "09/2030", "123", 20500.00, "Tom Jobim")

compra_farmacia = Compra(50.0, "2023-08-11", "Medicamentos", "Farmacia ABC", visa)
compra_restaurante = Compra(89.9, "09-11-2023", "Burguer King", "Lazer", visa)
compra_supermercado = Compra(500.0, "09-11-2023", "Supermercado Dia", "Alimentação", visa)

print(compra_farmacia) 
print(compra_restaurante)
print(compra_supermercado)
print()

compra_amazon = Compra(1000.0, '15/02/2023 19:46:17', 'Amazon', 'Casa',visa, 10)
print(f'Compra a crédito: {compra_amazon.valor} em {compra_amazon.quantidade_parcelas}')

fatura = [compra_farmacia, compra_restaurante, compra_supermercado, compra_amazon]
total = 0
for compra in fatura:
    total += compra.valor
print(f'O total da fatura é: {total}')