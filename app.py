menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova Conta
[nu] Novo Usuario
[q] Sair
"""

AGENCIA = "0001"
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
contas = []
usuarios = []


def deposito(saldo, extrato, /):
    valor = float(input("Informe o valor do deposito: "))
    if valor <= 0:
        print("Informe um valor maior que 0")
    else:
        saldo += valor
        extrato = (
            f"Deposito realizado no valor de R$ {valor:.2f}, novo saldo: R$ {saldo:.2f}"
        )
        print(extrato)
        return extrato, saldo


def saque(*, saque, saldo, extrato, numero_saques):
    if saque <= saldo:
        if saque <= limite:
            saldo -= saque
            extrato += f"\nSaque realizado no valor de R$ {saque:.2f}"
            numero_saques += 1
            print(extrato)
            return saldo, extrato, numero_saques
        else:
            print(
                f"O saque de R$ {saque:.2f} é maior que o limite por operação de {limite}"
            )
            return saldo, extrato, numero_saques
    else:
        print(f"você não tem saldo suficiente: R$ {saque:.2f}")
        return saldo, extrato, numero_saques


def extratos(saldo, /, *, extrato):
    print("\n-----------Extrato------------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("------------------------------------")


def filtar_usuario(cpf, usuarios):

    usuario = [user for user in usuarios if user["cpf"] == cpf]
    return usuario[0] if usuario else None


def criar_usuario(usuarios):

    cpf = input("Informe o CPF (Somente numeros): ")
    usuario = filtar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário já cadastrado")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/estado): ")

    usuarios.append(
        {
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco,
        }
    )
    print("Usuario criado")


def criar_conta_corrente(agencia, numero_conta, usuarios):

    cpf = input("informe o CPF do usuario: ")
    usuario = filtar_usuario(cpf, usuarios)
    if usuario:
        print("Conta criada com sucesso")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuario não encontrado")


while True:
    opcao = input(menu)

    if opcao == "d":
        extrato, saldo = deposito(saldo, extrato)

    elif opcao == "s":

        if not saldo:
            print("Sem saldo para saca")
        else:
            v_saque = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = saque(
                saque=v_saque, saldo=saldo, extrato=extrato, numero_saques=numero_saques
            )
        if numero_saques > LIMITE_SAQUES:
            print("Você atingiu o limite de 3 saques")

    elif opcao == "e":
        extratos(saldo, extrato=extrato)
    elif opcao == "nu":
        criar_usuario(usuarios)
    elif opcao == "nc":
        num_conta = len(contas) + 1
        conta = criar_conta_corrente(AGENCIA, num_conta, usuarios)
        if conta:
            contas.append(conta)
    elif opcao == "q":
        break
    else:
        print("Operação invalida")
        break
