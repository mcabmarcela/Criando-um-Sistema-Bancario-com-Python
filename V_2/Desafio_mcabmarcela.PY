import random

def gerador_de_numeros(numero_conta_cadastradas):
    numero_conta_cadastradas = []

    conta_tmp = "{:04d}".format(random.randint(1, 4000))
    digito_tmp = '-'+str( random.randint(1, 9))
    numero_tmp_conta = str(conta_tmp)+digito_tmp

    if numero_tmp_conta not in numero_conta_cadastradas:
        numero_da_conta = numero_tmp_conta
        numero_conta_cadastradas.append(numero_tmp_conta)

    elif numero_tmp_conta in numero_conta_cadastradas:
        while numero_tmp_conta in numero_conta_cadastradas:
            conta_tmp = "{:04d}".format(random.randint(1, 4000))
            digito_tmp = '-'+str( random.randint(1, 9))
            numero_tmp_conta = str(conta_tmp)+digito_tmp
        
        numero_da_conta = numero_tmp_conta

    return numero_conta_cadastradas, numero_da_conta


def menu_principal():
    return input( """
======== BEM VINDO ========
| ESCOLHA A OPÇÃO DESEJADA |
|--------------------------|
| [1] Depositar            |
| [2] Sacar                |
| [3] Extrato              |
| [4] Cadastrar Usuário    |
| [5] Cadastrar Conta      |
| [6] Consulta Dados       |
| [7] Sair                 |
|__________________________|

=> """)


def alterar_limite(LIMITE_SAQUES, limite, numero_saques, soma_de_saques, soma_alteracao_limite):
    opcao_alterar_limite = int(input(f"""
============== BEM VINDO ===============
         LIMITES PERMITIDOS            
----------------------------------------
 Nº de Saque Diário - 0{LIMITE_SAQUES}                    
 Valor de Saque Diário - R${limite:.2f}     
________________________________________
         TRASAÇÕES REALIZADAS          
----------------------------------------
 Nº de Saque realizados - 0{numero_saques}               
 Valor de Saque realizados - R${soma_de_saques:.2f} 
________________________________________
      DESEJA ALTERAR OS LIMITES?       
----------------------------------------
 [1] SIM                                   
 [2] NÃO                               
________________________________________


=> """))
    if opcao_alterar_limite == 1:
        if soma_alteracao_limite >= 2:
            print('============================================================')
            print('  Limite só pode ser alterado até duas vezes no mesmo dia.')
            print('  Tente novamente amanhã .. ')
            print('============================================================')

        elif soma_alteracao_limite < 2:   
            LIMITE_SAQUES = int(input('Digite a nova quantidade de saque diários: '))
            limite = float(input('Digite o novo valor de saque diários: '))
            soma_alteracao_limite += 1

    return LIMITE_SAQUES, limite, soma_alteracao_limite


def deposito(valor, saldo, extrato):

        if valor > 0:
            saldo += valor
            extrato += f' Depósito: R$ {valor:.2f}\n'
            print('===================================')
            print('  Depósito realizado com sucesso')
            print('===================================')

        else:
            print('=========================================')
            print('  ATENÇÃO! O valor informado é inválido.')
            print('=========================================')

        return saldo, extrato


def sacar(saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES, soma_de_saques, soma_alteracao_limite):
        
        excedeu_saldo = valor > saldo
        excedeu_limite = (soma_de_saques + valor) > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES        

        if excedeu_saldo:
            print('===========================================')
            print('  ATENÇÃO! Você não tem saldo suficiente.')
            print('===========================================')

        elif excedeu_limite:
            print('==========================================================')
            print(' ATENÇÃO! O valor do saque irá exceder o limite permitido.')
            print('==========================================================')

            LIMITE_SAQUES, limite, soma_alteracao_limite = alterar_limite (
            LIMITE_SAQUES, limite, numero_saques, soma_de_saques, soma_alteracao_limite=soma_alteracao_limite)
            
        elif excedeu_saques:
            print('=============================================')
            print('  ATENÇÃO! Número máximo de saques excedido.')
            print('=============================================')

            LIMITE_SAQUES, limite, soma_alteracao_limite = alterar_limite (
            LIMITE_SAQUES, limite, numero_saques, soma_de_saques, soma_alteracao_limite=soma_alteracao_limite)

        elif valor > 0:
            saldo -= valor
            extrato += f' Saque: R$ {valor:.2f}\n'
            numero_saques += 1
            soma_de_saques = soma_de_saques + valor

        else:
            print('===========================================')
            print('   ATENÇÃO! O valor informado é inválido.')
            print('===========================================')

        return saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES, soma_de_saques, soma_alteracao_limite 


def extrato(saldo, extrato, numero_saques, soma_de_saques):
        print('\n==================== EXTRATO =====================')
        print(' Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\n Saldo: R$ {saldo:.2f}')
        print('===================================================')
        print(' Quantidade de saque realizados hoje: ', numero_saques)
        print(' Soma de valores retirados hoje: R$', soma_de_saques)
        print('===================================================')


def verificar_cpf(cadastro_de_usuario):
    cpf = input('Digite seu CPF - ')

    '''
    while len(cpf) < 11:
        print('CPF Inválido, CPF deve conter 11 digitos')
        cpf = input('Digite seu CPF - ')
    '''
    verificacao = [cadastro_de_usuario[i] for i in cadastro_de_usuario if cpf == i] or [False for i in cadastro_de_usuario if cpf != i]
    
    if verificacao == [] or False in verificacao:
        cadastro = 0
    else:
        cadastro = 1

    return verificacao, cpf, cadastro


def verificar_contas(contas_cadastradas, cpf):
    conta = [contas_cadastradas[i] for i in contas_cadastradas if cpf == i] or [False for i in contas_cadastradas if cpf != i]
    
    if conta == [] or False in conta:
        cadastro_conta = 0
    else:
        cadastro_conta = 1

    return conta, cadastro_conta


def cadastrar_usuarios(cpf, chave_usuario, cadastro_de_usuario):
    dados_tpm_1={}
    print("""
=================== INSTRUÇÕES =====================
    DATAS: dd/mm/aaaa   | CPF: SOMENTE NUMEROS
     Ex: 27/12/1993     |   Ex: 01823245689
====================================================
""")
    for chave in chave_usuario:
        print(f'Digite {chave}: ', end='')
        dados_tpm_1[chave] = input()

    dados_tpm = dict.fromkeys([cpf], dados_tpm_1)
    cadastro_de_usuario.update(dados_tpm)

    return cadastro_de_usuario


def cadastro_contas(cadastro_de_usuario, contas_cadastradas, numero_conta_cadastradas):
    AGENCIA = "0001"
    verificacao, cpf, cadastro = verificar_cpf(cadastro_de_usuario)

    if cadastro == 0:
        print("""
===========================================
  Não há usuários cadastrado com esse CPF 
===========================================""")
        
        
    if cadastro == 1:
        numero_conta_cadastradas, numero_da_conta = gerador_de_numeros(numero_conta_cadastradas)

        if cpf not in contas_cadastradas: 
            
            contas_cadastradas[cpf]={}        
            busca_nome = [cadastro_de_usuario[cpf]['Nome'] for i in cadastro_de_usuario if cpf == i]
            contas_cadastradas[cpf]['Titular_da_Conta'] = busca_nome[0]
            contas_cadastradas[cpf]['Agencia'] = AGENCIA 
            contas_cadastradas[cpf]['Numero_da_Conta'] =[numero_da_conta]
            print("""
==================================
   conta cadastrada com sucesso 
==================================""")

        else:
            contas_cadastradas[cpf]['Numero_da_Conta'].append(numero_da_conta)
            print("""
=====================================
  Nova conta cadastrada com sucesso 
=====================================""")

    return contas_cadastradas, numero_conta_cadastradas


def consulta_dados(cadastro_de_usuario, cpf, conta_de_usuarios):
    MENU_CONSULTA = int(input("""
.__________________________.
|        CONSULTAR         |
|--------------------------|
| [1] Contas               |
| [2] Usuários             |
|__________________________|

=> """))

    verificacao, cpf, cadastro = verificar_cpf(cadastro_de_usuario)
    if cadastro == 0:
        print("""
===========================================
  Não há usuários cadastrado com esse CPF 
===========================================""")

    elif MENU_CONSULTA == 2:
        for i in cadastro_de_usuario:
            if i == cpf: 
                print('==============================================================')
                print('CPF - ',i)
                for j in cadastro_de_usuario[i]:
                    print(j,'-', cadastro_de_usuario[i][j])
                print('==============================================================')

    elif MENU_CONSULTA == 1:
        conta, cadastro_conta = verificar_contas(conta_de_usuarios, cpf) 
        if cadastro_conta == 1:
            for i in conta_de_usuarios:
                if i == cpf:
                    print('='*80)
                    print('  CPF: ', i, end='  -  ')
                    for chave, valor in conta_de_usuarios[i].items():
                        if chave == 'Titular_da_Conta':
                            print('  Titular da Conta:', valor)
                            print('='*80)
                            print(" "*8,'CONTA CADASTRADOS')
                            print('-'*80)
                        if chave == 'Numero_da_Conta':
                            for NUMERO_DA_CONTA in valor:
                                print('  Agencia: 0001          C/C:', NUMERO_DA_CONTA) 
                                
        elif MENU_CONSULTA != 1 and MENU_CONSULTA != 2:
            print('Opção inválida')    
        else:
            print("""
===========================================
  Não há Contas cadastrada para esse CPF 
===========================================""")

    else:
        print('Opção inválida')


def principal():

    LIMITE_SAQUES = 3

    saldo = 0
    extratos = ""
    limite = 3000
    soma_alteracao_limite=0
    soma_de_saques = 0
    numero_saques = 0
    #chave_usuario = ('Nome', 'Data de Nascimento')
    chave_usuario = ('Nome', 'Data de Nascimento', 'Rua', 'Nº', 'Bairro', 'Cidade', 'UF')
    cadastro_de_usuario = {}
    cpf=''  
    verificacao = ''
    contas_cadastradas = {}
    numero_da_conta = ''
    cadastro = 0
    numero_conta_cadastradas = []

    while True:

        opcao = menu_principal()

        if opcao == '1': #DEPOSITO
            valor = float(input('Informe o valor do depósito: R$'))
            saldo, extratos = deposito(valor, saldo, extratos)

        elif opcao == '2': #SACAR
            valor = float(input('Informe o valor do saque: R$'))
            saldo, valor, extratos, limite, numero_saques, LIMITE_SAQUES, soma_de_saques, soma_alteracao_limite = sacar(
            saldo=saldo, valor=valor, extrato=extratos, limite=limite, numero_saques=numero_saques, 
            LIMITE_SAQUES=LIMITE_SAQUES, soma_de_saques=soma_de_saques, soma_alteracao_limite=soma_alteracao_limite
                                    )
            
        elif opcao == '3': #EXTRATO
            extrato(saldo, extrato=extratos, numero_saques=numero_saques, soma_de_saques=soma_de_saques)

        elif opcao == '4': #CADASTRAR USUÁRIO
            verificacao, cpf, cadastro = verificar_cpf(cadastro_de_usuario=cadastro_de_usuario)

            if cadastro == 0:
                cadastro_de_usuario = cadastrar_usuarios(cpf=cpf, chave_usuario=chave_usuario, 
                                                        cadastro_de_usuario=cadastro_de_usuario)            
            else:
                print('=========================')
                print('  Usuário já cadastrado')
                print('=========================')
 
        elif opcao == '5': #CADASTRAR CONTA
            contas_cadastradas, numero_conta_cadastradas = cadastro_contas(cadastro_de_usuario=cadastro_de_usuario, 
                                                                           contas_cadastradas=contas_cadastradas,
                                                                           numero_conta_cadastradas=numero_conta_cadastradas)

        elif opcao == '6': #CONSULTAS
            consulta_dados(cpf=cpf, 
                           cadastro_de_usuario=cadastro_de_usuario,
                           conta_de_usuarios=contas_cadastradas)                
                
        elif opcao == '7': #SAIR
            break

        else:
            print('==============================================================')
            print('  ATENÇÃO, por favor selecione novamente a operação desejada.')
            print('==============================================================')
    
principal() 
print("""
=========================
        Obrigada!       
=========================           
      """)         