from excecoes import ValorExcedidoException

from random import randint
from datetime import date 
from dateutil.relativedelta import relativedelta

def cria_numero_do_cartao():
    grupos_de_numeros = [f'{randint(1, 999): 04}' for i in range (4)]
    return ''.join(grupos_de_numeros)  

def cria_cvv_do_cartao():
  cvv = f'{randint(1, 999): 03}'
  return cvv

def define_validade_do_cartao():
  validade = date.today() + relativedelta(years= 4, months= 6, day= 31)
  return validade

class Cartao:
 def __init__(self, numero, validade, cvv, limite, cliente, id=None):
  self.__numero = numero
  self.__validade = validade
  self.__cvv = cvv
  self.__set__limite(limite)
  self.__set_cliente(cliente)
  self.__status = 'ATIVO'
  self.__id = id

  def cancela(self):
    self.__status = 'CANCELADO'

  def ativa(self):
    self.__status = 'ATIVO'

  @property 
  def id(self):
    return self.__id
  
  @property
  def numero(self):
    return self.__numero
  
  @property
  def validade(self):
    return self.__validade
  
  @property
  def cvv(self):
    return self.__cvv
  
  @property
  def limite(self):
    return self.__limite
  
  @limite.setter
  def limite(self, limite):
    self.__set = limite(limite)

  @property
  def cliente(self):
    return self.__cliente
  
  @property
  def status(self):
    return self.__status
  
  def __str__(self):  
    return f'Cartão(#{self.id}) {self.numero} do(a) {self.cliente} com limite de {self.limite} válido até {self.validade}'
  
  def __set__limite(self, limite):
    limite_minimo = 10
    if limite < limite_minimo:
     raise ValueError(f'O limite deve ser de no mínimo {limite_minimo}')
    
    class Compra:
     def __init__(self, valor, data, estabelecimento, categoria, cartao, id=None):
      self.__set__valor(valor)
      self.__data = data
      self.__set__estabelecimento(estabelecimento)
      self.__categoria = categoria.strip()
      self.__set__cartao(cartao)
      self.__id = id
      self.valida_compra()

      def __set__estabelecimento(self, estabelecimento):
         tamanho_estabelecimento = len(estabelecimento)
         limite_caracteres = 30
         if tamanho_estabelecimento > limite_caracteres:
          raise ValueError(f"estabelecimento com {tamanho_estabelecimento} caractere é superior ao limite de {limite_caracteres} caractere")
      
      def _set_valor(self, valor):
        if valor <= 0:
         raise ValueError(f"o valor {valor} deve ser superior a zero")
       
      def _set_cartao(self, cartao):
       if cartao is None:
         raise ValueError("É obrigatório um cartão")
       
       def valida_compra(self):
         limite = self._cartao.limite
         valor = self._valor
         if valor > limite:
           valor_excedido = valor- limite
           raise ValorExcedidoException(f'O valor da compra excedeu ${valor_excedido} do limite')
         

         

