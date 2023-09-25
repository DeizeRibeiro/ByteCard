from use_case import lista_cartoes, pesquisa_cartao_por_id, cadastra_cartao, cadastra_compra, lista_compras, monta_relatorio_gastos_por_categoria

todos_os_cartoes = lista_cartoes()
print(f'Cartões pré-cadastrados: {len(todos_os_cartoes)}')  

cartao_existente = pesquisa_cartao_por_id(1)
cartao_inexistente = pesquisa_cartao_por_id(1000)
print(f'Cartão existente: {cartao_existente}')
print(f'Cartão inexistente: {cartao_inexistente}')

cadastra_cartao('Diana Prince', 5500.0)
for cartao in lista_cartoes():
 print(cartao)

 cadastra_compra(2, 100.0, 'Alimentação', 'Pizzaria Dominos')
 cadastra_compra(2, 150.0, 'Lazer', 'Show de pagode')
 cadastra_compra(3, 200.0, 'Alimentação', 'Rodízio de comida japonesa')
 cadastra_compra(3, 250.0, 'Lazer', 'Show de rock')
 cadastra_compra(3, 300.0, 'Educação', 'Assinatura da Alura')

 for compra in lista_compras():
  print(compra)

  gastos_pos_categoria = monta_relatorio_gastos_por_categoria()
for categoria, total in gastos_pos_categoria.items():
 print('Gastos por categoria:')
 print(categoria, '-', total)