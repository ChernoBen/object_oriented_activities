from clients import Client
from accounts import Account,SpecialAccount
from banks import Bank

 
joao = Client('Joao da Silva','777-1234')
maria = Client('Maria da Silva','555-4321')
contam = Account(maria,99)
contaj = Account(joao,100)
tatu = Bank("Tatú")
tatu.abre_conta(contaj)
tatu.abre_conta(contam)
tatu.lista_contas()
contaJoao =SpecialAccount(joao,2,500,1000)
contaJoao.deposito(1000)
contaJoao.deposito(3000)
contaJoao.deposito(95.15)
contaJoao.saque(1500)
contaJoao.extrato()

