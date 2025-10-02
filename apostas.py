from random import randint

dinheiro = 100 # Pode ser alterado
numero_da_sorte = randint(1, 10) # Tambem pode ser alterado
 
while dinheiro > 0:
    entrada_dinheiro = int(input('>>> Deposite o valor aqui: ')) # Deposito do dinheiro
    entrada_chute = int(input('>>> Agora qual sera o numero da sorte ?: '))
        
    if entrada_dinheiro > dinheiro:
        print('!!! Valor maior do que voce tem !!!')
        print(f"-- Saldo atual: {dinheiro} --")
        
    elif entrada_dinheiro == 0:
        print('!!! Voce colocou um valor nulo !!!')
        print(f"-- Saldo atual: {dinheiro} --")
        
    if entrada_chute == numero_da_sorte:
        print(f'*** Voce acertou! Seu saldo foi dobrado: {entrada_dinheiro * 2} ***')
        dinheiro += entrada_dinheiro * 2 # Pode ser alterado
        print(f"-- Saldo atual: {dinheiro} --")
        
    elif entrada_chute != numero_da_sorte:
      if entrada_dinheiro < 101: # Pode ser alterado
       print(f'XXX Voce nao acertou e perdeu: {entrada_dinheiro} reais XXX')
       dinheiro -= entrada_dinheiro
       print(f"-- Saldo atual: {dinheiro} --")

# HukBross -> 01/10/2025
# Alaxendre -> 01/10/2025
