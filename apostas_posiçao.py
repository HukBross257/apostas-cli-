from random import shuffle
# Versao de posiçoes da aposta !
# A cada rodada a lista é embaralhada e voce deve achar a posiçao do 5 apois isso.

dinheiro = 100 # Valor podera ser alterado

while dinheiro > 0:
    lista_adivinhar = ['-', '-', '-', '-', '-', '-', 5]
    shuffle(lista_adivinhar)
    
    entrada_dinheiro = int(input('>>> Deposite o valor aqui: ')) # Deposito do dinheiro
    entrada_chute = int(input(f'>>> Agora qual sera a posiçao do <5> ?:'))
    lista_posiçao = lista_adivinhar.index(5)
    
    
        
    if entrada_dinheiro > dinheiro:
        print('!!! Valor maior do que voce tem !!!')
        print(f"-- Saldo atual: {dinheiro} --")
        
    elif entrada_dinheiro == 0:
        print('!!! Voce colocou um valor nulo !!!')
        print(f"-- Saldo atual: {dinheiro} --")
        
    if entrada_chute == lista_posiçao:
        print(f'*** Voce acertou! Seu saldo foi dobrado: {entrada_dinheiro * 2} ***')
        dinheiro += entrada_dinheiro * 2 # Pode ser alterado
        print(f"-- Saldo atual: {dinheiro} --")
        
    elif entrada_chute != lista_posiçao:
      if entrada_dinheiro < 101: # Pode ser alterado
       print(f'XXX Voce nao acertou e perdeu: {entrada_dinheiro} reais XXX')
       dinheiro -= entrada_dinheiro
       print(f"-- Saldo atual: {dinheiro} --")
       print(f"-- Resposta Correta: {lista_posiçao}")
       print(f'--> Lista completa : {lista_adivinhar}')

# HukBross -> 01/10/2025
# Alaxendre -> 01/10/2025


