# Criando um Sistema Bancario com Python


 ## 💪🏾 Desafio proposto

Criar um sistema bancários com algumas operações.

## 🥈 2ª Versão
Para fins de deixar o código mais modularizado, para isso vamos criar funções para as operações existentes: 
 - sacar, depositar e visualizar histórico. 
 - Além disso, para a versão 2 do nosso sistema precisamos criar duas novas funções: 
   - criar usuário (cliente do banco) (cpf, nome, Dt. Nascimento, endereço(rua, nº, bairro, cidade, UF))
   - criar conta corrente (vincular com usuário) (cpf, agencia = 0001, conta = sequencial iniciando em 1)

## Solução apresentada.. 🤓

Desenvolvido sistema contendo as operações:

## -> Funções
 Saque, Deposito, Extratos, Alterar Limites (limitado a duas alterações), Gerador Automático e aleatório de Contas com digitos, Consultar cadastros (Contas e usuário).

 - Cadastros de usuário - não podendo haver dois cadastros para o mesmo usuário
 ---
 - Um usuário pode ter várias contas, uma coisa pode ter só um Titular
 ---
 - Não adiciona vários cadastros de contas com o mesmo Titular, adiciona a conta no cadastro do Titular.

---

--

## 🥇 1ª Versão
Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.
Sendo que o usuário deve realizar:
 - Somente 3 saques ao dia 
 - Limite de R$ 500,00 por saque 
 - Não pode ter saldo negativo
 - Visualizar extrado com todas as movimentações.

## Solução apresentada.. 🤓

Desenvolvido sistema contendo as operações:
- Saque
   - Inicialmente, somente 3 saques ao dia 
   - Limite de R$ 3000,00 por dia
---
 - Depositos
 ---
 - Extratos
   - Visualizar extrado com todas as movimentações.
 ---
 - Opção de Alterar Limite Inicial
    - Limitado a duas alteração ao dia
---





