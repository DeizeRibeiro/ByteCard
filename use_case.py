from datetime import date, datetime
from collections import defaultdict
from model import Cartao, Compra, cria_cvv_do_cartao, cria_numero_do_cartao, define_validade_do_cartao

sequencia_ids = 1

banco_cartoes = {}
banco_compras = []

def lista_cartoes():
 return list(banco_cartoes.values())

def pesquisa_cartao_por_id(id):
 return banco_cartoes.get(id)

def cadastra_cartao(cliente, limite):
 global sequencia_ids
 numero = cria_numero_do_cartao()
 cvv = cria_cvv_do_cartao()
 validade = define_validade_do_cartao()
 limite = 1000.0
 cliente = cliente
 novo_cartao = Cartao(numero=numero, validade=validade, cvv=cvv, limite=limite, cliente=cliente, id=sequencia_ids)
 sequencia_ids += 1

def cadastra_compra(cartao_id, valor, categoria, estabelecimento):
 global sequencia_ids
 cartao = pesquisa_cartao_por_id(cartao_id)
 agora = datetime.now()
 nova_compra = Compra(valor=valor, categoria=categoria, estabelecimento=estabelecimento, cartao=cartao, data=agora, id=sequencia_ids)
 banco_compras.append(nova_compra)
 sequencia_ids += 1

def lista_compras():              
  return banco_compras

def monta_relatorio_gastos_por_categoria():
 gasto_por_categoria = defaultdict(float)
 for compra in lista_compras():
  gasto_por_categoria[compra.categoria] += compra.valor
  return gasto_por_categoria

cartao1 = Cartao(cria_numero_do_cartao(), date(2031, 1, 31), '321', 1000.0, 'Steve Rogers', id=1)
cartao2 = Cartao(cria_numero_do_cartao(), date(2035, 5, 31), '789', 2000.0, 'Matt Murdock', id=2)
cartao3 = Cartao(cria_numero_do_cartao(), date(2029, 5, 31), '887', 10000.0, 'Bruce Wayne', id=3)

banco_cartoes = {cartao1.id: cartao1, cartao2.id: cartao2, cartao3.id:cartao3}   

from collections import defaultdict
from datetime import date
from datetime import datetime
from random import randint
from dateutil.relativedelta import relativedelta

from model import Cartao, Compra

def cria_numero_do_cartao():
    grupos_de_numeros = [f'{randint(1, 999): 04}' for i in range (4)]
    return ''.join(grupos_de_numeros)  

def cria_cvv_do_cartao():
  cvv = f'{randint(1, 999): 03}'
  return cvv

def define_validade_do_cartao():
  validade = date.today() + relativedelta(years= 4, months= 6, day= 31)
  return validade































