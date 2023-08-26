from lampada import Lampada
from conta import Conta, ContaPoupanca


conta_pedro = Conta(123, 147, "Pedro")
conta_pedro.depositar(1000)
print(f"saldo de {conta_pedro.titular} é {conta_pedro.saldo}")


conta_jose = Conta(456, 123, "Jose")
conta_jose.depositar(1000)
print(f"saldo de {conta_jose.titular} é {conta_jose.saldo}")

conta_pedro.transferir(250,conta_jose)

print(f"saldo de {conta_pedro.titular} é {conta_pedro.saldo}")
print(f"saldo de {conta_jose.titular} é {conta_jose.saldo}")



conta_daniele = ContaPoupanca(963,854, "Daniele")
conta_daniele.
