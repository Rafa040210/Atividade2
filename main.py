from conta import Conta

obj_conta = Conta(float(input("Qual é o saldo da conta? ")))

#EXIBIR UM MENU
input("Escolha uma opção: ")
print("---- MENU DE OPÇÕES ----")
print("1 - Sacar")
print("2 - Deposita")
print("3 - Rendimento")
if opcao == 1:
    obj_conta.saca(float(input("Qual o valor a sacar: ")))
    print("Seu valor na conta é:", obj_conta.saldo)
elif opcao == 2:
    obj_conta.deposita(float(input("Qual o valor a deposita: ")))
    print("Seu valor na conta é:", obj_conta.saldo)
elif opcao == 3:
    obj_conta.rendimento(float(input("Qual o valor do rendimento: ")))
    print("Seu valor na conta é:", obj_conta.saldo)
