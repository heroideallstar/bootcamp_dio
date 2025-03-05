menu = """=======================================
Olá! bem vindo a sua conta DIO...
========================================
    O que deseja fazer?
    [d] depósitos      
    [s] saques         
    [e] extratos       
    [q] sair           
"""
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
SAQUE_DIARIO = 500
while True:
    opcao = input(menu)
    if opcao == "d":
        valor = float(input("Digite o valor do depósito:R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Deposito R$ {valor:.2f}\n" 
        else:
            print("O valor informado é invalido, favor tente novamente...\n")
    elif opcao == "s":
        valor = float(input("Digite o valor do saque:R$ "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        if excedeu_saques:
            print("Numero de saques excedido, favor tente mais tarde...\n")
        elif excedeu_saldo:
            print("Não há saldo o suficiente para completar esta transação...\n")
        elif excedeu_limite:
            print(f"O limite desta transação é de R$ {limite:.2f}, favor, tentar novamente...\n")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n" 
            numero_saques += 1
        else:
            print("Falha na transação, o valor informado é inválido...\n")
    elif opcao == "e":
        print("\n===============Extrato===============")
        print("Não foram realizadas transações" if not extrato else extrato)
        print(f"\nSaldo R$ {saldo:.2f}")
        print("=======================================")
    elif opcao == "q":
        break
    else:
        print("Opção invalida, por favor, tente novamente...\n")
