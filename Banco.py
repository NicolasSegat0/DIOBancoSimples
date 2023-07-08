menu = '''
[1] Depositar 

[2] Sacar 

[3] Extrato 

[0] Sair
'''



saldo = 0
limite = 500 
extrato = ''
numero_saques = 0
MAXIMO_SAQUE = 3

print('Bem vindo ao Banco NNS!')
print()

while MAXIMO_SAQUE: 
    resposta = int(input(menu))
    print()

    if resposta == 1: 
        valor = int(input('Digite um valor para deposito: '))

        if valor > 0: 
            saldo += valor
            print('O valor atual é de {}'.format(valor))
        else: 
            print('A operação não pode ser efetuada')

    if resposta == 2: 
        valor = int(input('Insira o valor que queira sacar: '))

        excedeu_saldo = valor > saldo 
        excedeu_limite = valor > limite 
        excedeu_saques = numero_saques >= MAXIMO_SAQUE

        if excedeu_saldo: 
            print('Operação falhou!')
        elif excedeu_limite: 
            print('Operação falhou!')
        elif excedeu_saques: 
            print('Operação falhou!')
        elif valor > 0: 
            
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1

        else: 
            print('Operação falhou')

    
    elif resposta == 3: 
        print('\n======Extrato======')
        print('Não foram realizadas movimentações.' if not extrato else extrato)
        print(f'\nSaldo: R$ {saldo:.2f}')
        print('=======================')

    elif resposta == 0: 
        break

    else: 
        print('Operação inválida. Volte para o menu.')



