def depositar (saldo, valor , extrato):
    if saldo >= 0:
        saldo += valor
        extrato += f"Depósito: R${valor: .2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES
    
    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R${valor: .2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n===============EXTRATO==================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo: .2f}")
    print("========================================")
    
menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
    => """     
    
def main():
    
    LIMITE_SAQUES = 3
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    
    while True:
        opcao = input(menu)
        
        if opcao == "1":
            valor = float(input("Informe o valor de depósito:"))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "2":
            valor = float(input("Informe o valor do saque:"))
            saldo, extrato, numero_saques = sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES)
        
        elif opcao == "3":
            exibir_extrato(saldo, extrato)
            
        elif opcao == "0":
            break
        
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")
        
main()
        
        