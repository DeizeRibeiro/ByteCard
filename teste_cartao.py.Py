from model import Cartao

visa = Cartao("4234 5678 9012 3456", "09/2030", "123", 20500.00, "Tom Jobim")
master = Cartao("5194 5438 9312 3488", "10/2031", "455", 110500.00, "Thiago Andrade")

print(visa.status)
print(master.status)
visa.cancela()
print(visa)
visa.ativa()
print(visa)
master.cancela()

# linhas anteriores omitidas.
visa.limite = 7000.0
master.limite = 9500.0
print(visa.limite)
print(master.limite)

