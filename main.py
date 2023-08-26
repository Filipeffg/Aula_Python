from lampada import Lampada
from conta import  ContaPoupanca, ContaCorrente

conta_jose = ContaCorrente(456, 123, "Jose")
conta_jose.depositar(1000)
print(conta_jose)

conta_daniele = ContaPoupanca(963,854, "Daniele")
conta_daniele.depositar(1000)
print (conta_daniele)

conta_jose.sacar(1600)
print(conta_jose)
