# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 16:04:57 2021

@author: Fábio dos Reis
"""

import random
import time

def mostraIntro():
    print('''Duas cavernas, uma à esquerda e uma à direita. Ambas
          possuem tesouros guardados por duendes. Escolha uma caverna para explorar''')
    print()
    
def escolherCaverna():
    caverna = 0
    escolha = ''
    while escolha != 'E' and escolha != 'D':
        print('Escolha a caverna: E ou D')
        escolha = input()
        if (escolha == 'E'):
            caverna = 1
        if (escolha == 'D'):
            caverna == 0
    return caverna

def verificaCaverna(caverna):
    print('Você está na entrada da caverna...')
    time.sleep(3)
    print('A caverna é escura e assustadora...')
    time.sleep(3)
    print('De repente, um duende surge da escuridão bem em frente a você!')
    print()
    time.sleep(2)
    
    duendeAmistoso = random.randint(0, 1)

    if caverna == duendeAmistoso:
        print('Seja bem-vindo e vamos compartilhar o tesouro!')
    else:
        print('Diga adeus invasor, vou te matar agora!')
        time.sleep(5)
        combateOuFuga()
        
    print(duendeAmistoso)  

def combateOuFuga():
    print('Você precisa decidir o que irá fazer. Irá fugir?')
    print('Ou irá enfrentar o duende para tentar obter seu tesouro?\n')
    time.sleep(4)
    print('Digite F se for covarde ou L se for valente e decidir lutar!')
    decisao = input()
    if decisao == 'F':
        print('Fuja covarde!')
    if decisao == 'L':
        print('Saque sua espada imediatamente!')

mostraIntro()
caverna = escolherCaverna()
verificaCaverna(caverna)

print('')