from conta import Conta

obj_conta = Conta(float(input("Qual é o saldo da conta? ")))


print("---- MENU DE OPÇÕES ----")
print("1 - Sacar")
print("2 - Deposita")
print("3 - Rendimento")
opcao = int(input("Escolha uma opção: "))


if opcao == 1:
    obj_conta.saca(float(input("Qual o valor a sacar: ")))
    print("Seu valor na conta é:", obj_conta.saldo)
elif opcao == 2:
    obj_conta.deposita(float(input("Qual o valor a deposita: ")))
    print("Seu valor na conta é:", obj_conta.saldo)
elif opcao == 3:
    print("Seu valor na conta é:", obj_conta.saldo)
