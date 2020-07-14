class Account:
  def __init__(self,cliente,numero,saldo=0):
    self.saldo = saldo
    self.clientes = cliente
    self.numero = numero
    self.operacoes = []
    self.deposito(saldo)
    self.nome = self.clientes.nome
    self.telefone = self.clientes.telefone
  
  def resumo(self):
    print("CC Número: %s Saldo : %10.2f"%(self.numero,self.saldo))
  
  def saque(self,valor):
    if self.saldo >=valor:
      if valor - self.saldo < 0:
        return print("valor indisponivel")
      self.saldo-=valor
      self.operacoes.append(["SAQUE",valor])

  def deposito(self,valor):
    self.saldo +=valor
    self.operacoes.append(["DEPOSITO",valor])
  
  def extrato(self):
    print("Extrato CC N %s\n"% self.numero)
    for o in self.operacoes:
      print("%10s %.2f"%(o[0],o[1]))
    print("\n  Saldo: %10.2f\n"% self.saldo)




class SpecialAccount(Account):
  def __init__(self,clientes,numero,saldo=0,limite=0):
    Account.__init__(self,clientes,numero,saldo)
    self.limite = limite
  
  def saque(self,valor):
    if self.saldo+self.limite>=valor:
      self.saldo -=valor
      self.operacoes.append(['SAQUE',valor])