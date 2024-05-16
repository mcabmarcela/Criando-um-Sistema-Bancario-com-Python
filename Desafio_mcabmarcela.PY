menu_principal = """
======== BEM VINDO ========
| ESCOLHA A OPÇÃO DESEJADA |
|--------------------------|
| [1] Depositar            |     
| [2] Sacar                |
| [3] Extrato              |
| [4] Sair                 |
|__________________________|

=> """


saldo = 0
limite = 3000
soma_alteracao_limite=0
soma_de_saques = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3



menu_para_limite = f"""
============== BEM VINDO ===============
|         LIMITES PERMITIDOS            |
|---------------------------------------|
| Nº de Saque Diário - 0{LIMITE_SAQUES}               |     
| Valor de Saque Diário - R${limite:.2f}     |
|_______________________________________|


=> """

menu_para_alterar_limite = f"""
============== BEM VINDO ===============
|         LIMITES PERMITIDOS            |
|---------------------------------------|
| Nº de Saque Diário - 0{LIMITE_SAQUES}               |     
| Valor de Saque Diário - R${limite:.2f}     |
|_______________________________________|
|      DESEJA ALTERAR OS LIMITES?       |
|---------------------------------------|
| [1] SIM                               |     
| [2] NÃO                               |
|_______________________________________|


=> """


while True:

    opcao = input(menu_principal)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = (soma_de_saques + valor) > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES        

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")
            print(menu_para_limite)

            opcao_alterar_limite = int((input(menu_para_alterar_limite)))
            
            if opcao_alterar_limite == 1:
                if soma_alteracao_limite >= 2:
                    print('Limite só pode ser alterado até duas vezes no mesmo dia.')
                    print('Tente novamente amanhã .. ')

                elif soma_alteracao_limite < 2:   
                    LIMITE_SAQUES = int(input('Digite a nova quantidade de saque diários: '))
                    limite = float(input('Digite o novo valor de saque diários: '))
                    soma_alteracao_limite += 1



        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")


        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            soma_de_saques = soma_de_saques + valor

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "4":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")