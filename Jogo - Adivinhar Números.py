# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 11:54:52 2021

@author: Fábio dos Reis
"""

import random

numTentativas = 0

print("Qual o seu nome?")
nome = input()

num = random.randint(1, 20)
print('Olá {0}! Tente adivinhar um número entre 1 e 20.'.format(nome))
print('Você tem seis chances!')

for numTentativas in range(6):
    print('Digite o número.')
    tentativa = int(input())
    
    if tentativa < num:
        print('Você digitou um número baixo...')
    elif tentativa > num:
        print('Você digitou um número alto...')
    else:
        break
    
if tentativa == num:
    numTentativas = str(numTentativas + 1)
    print('Parabéns, {}!'.format(nome))
    print('Você adivinhou o número em {0} tentativas!'.format(numTentativas))
else:
    num = str(num)
    print('\nQue pena! O número era {0}!'.format(num))

