import textwrap #Adicionado depois de ver o video de solução da DIO

def menu():
    menu = """\n
    ========================================
    Olá! bem vindo a sua conta DIO...
    ========================================
    O que deseja fazer?
    [d]\tdepósitos      
    [s]\tsaques         
    [e]\textratos 
    [a]\tabrir uma conta DIO
    [c]\tcadastro de novo usuário
    [l]\tlista de contas
    [q]\tsair           
    """
    return input(textwrap.dedent(menu)) #Remove qualquer espaço em branco inicial em comum de toda linha em text.

def depositar(saldo, valor, extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Deposito:\tlR$ {valor:.2f}\n" 
        print("\n Depósito realizado com sucesso!")
    else:
        print("\nO valor informado é invalido, favor tente novamente...\n")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques
    if excedeu_saques:
        print("Numero de saques excedido, favor tente mais tarde...\n")
    elif excedeu_saldo:
        print("Não há saldo o suficiente para completar esta transação...\n")
    elif excedeu_limite:
        print(f"O limite desta transação é de R$ {limite:.2f}, favor, tentar novamente...\n")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n" 
        numero_saques += 1
    else:
        print("Falha na transação, o valor informado é inválido...\n")
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n===============Extrato===============")
    print("Não foram realizadas transações" if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("=======================================")

def criar_usuario(usuarios):
    cpf = input("informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n Já existe um usuario com este CPF! \n Se houver alguma inconsistencia, favor entrar em contato com sua agência.")
        return
    nome = input("Informe seu nome completo: ")
    data_nascimento = input("Informe sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe seu endereço (logadouro, numero - bairro - cidade/sigla do estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf":cpf, "endereco": endereco})
    print("Cadastro realizado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtratos = [usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuarios_filtratos[0] if usuarios_filtratos else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("informe o CPF (somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n Conta criada com sucesso!")
        return {"agencia":agencia, "numero_conta": numero_conta, "usuario":usuario}
    print("\n Usuário não encontrado, favor realizar seu cadastro ou entre em contato com sua agência")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 30)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    while True:
        opcao = menu()
        if opcao == "d":
            valor = float(input("Digite o valor do depósito:R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)
        elif opcao == "s":
            valor = float(input("Digite o valor do saque:R$ "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "c":
            criar_usuario(usuarios)
        elif opcao == "a":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "e":
            exibir_extrato(saldo, extrato = extrato)
        elif opcao == "l":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("Opção invalida, por favor, tente novamente...\n")
main()