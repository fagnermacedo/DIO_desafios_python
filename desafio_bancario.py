#Desafio Sistema Bancário com Python
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

==> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
contador_valor_saque = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        print(" ")
        valor_deposito = float(input("Infome o valor que você deseja depositar: "))
        saldo = saldo + valor_deposito
    
    elif opcao == "s":
        print("Saque")
        print(" ")
        
        valor_saque = float(input("Informe o valor que você deseja sacar: "))
        contador_valor_saque = valor_saque + contador_valor_saque

        if numero_saques > 3:
            print("Limite de saques diários  já alcançado")
        elif contador_valor_saque > 500:
            print("Limite diário atingido")
        elif valor_saque > saldo:
            print("Saldo insuficiente")
        else:
            print("Executando transação")
            saldo = saldo - valor_saque
        
        numero_saques = numero_saques + 1
    
    elif opcao == "e":
        print("Extrato")
        print(" ")
        print("Seu saldo atual é de: ", saldo)
    
    elif opcao == "q":

        break
    
    else:
        print("Opção escolhida não é válida")
