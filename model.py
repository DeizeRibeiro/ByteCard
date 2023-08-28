class Cartao:
  def __init__(self, numero, data_validade, cvv, limite, nome_cliente):
    self.__status = "ATIVO"
    self.__numero = numero
    self.__data_validade = data_validade
    self.__cvv = cvv
    self.__limite = limite
    self.__nome_cliente = nome_cliente

  def cancela(self):
    self.__status = "CANCELADO"

  def ativa(self):
    self.__status = "ATIVO"
  
  def __str__(self):
    return f"{self.__numero} - {self.__nome_cliente} - {self.__status}"
  
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
  @property
  def cliente(self):
   return self.__cliente
  @property
  def status(self):
   return self.__status
  
   class Compra:
    def __init__(self, valor, data, estabelecimento, categoria, cartao):
      self.__valor = valor
    self.__data = data
    self.__estabelecimento = estabelecimento
    self.__categoria = categoria
    self.__cartao = cartao

  def __str__(self):
    return f' Compra:{self.__valor} no dia {self.__data} em {self.__estabelecimento} no cartao {self.__cartao.numero}'

  class CompraCredito():
   def __init__(self, valor, data, estabelecimento, categoria, cartao, quantidade_parcelas):
    super().__init__(valor, data, estabelecimento, categoria, cartao)
    self.__quantidade_parcelas = quantidade_parcelas

@property
def valor(self):
  return ().valor*1.1
@property
def quantidade_parcelas(self):
  return self.__quantidade_parcelas 

@property
def valor_parcela(self):
  return self.valor / self.quantidade_parcelas

 

  



  
  
