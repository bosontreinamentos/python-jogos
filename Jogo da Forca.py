# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 12:05:10 2021

@author: Fábio dos Reis
"""

import random
from time import sleep
import os

FORCA = [
    '''
    +---+
        |
        |
        |
       ===
    ''',
    '''
    +---+
    O   |
        |
        |
       ===   
    ''',
    '''
    +---+
    O   |
    |   |
        |
       === 
    ''',
    '''
    +---+
    O   |
   /|   |
        |
       === 
    ''',
    '''
    +---+
    O   |
   /|\  |
        |
       === 
    ''',    
    '''
    +---+
    O   |
   /|\  |
   /    |
       === 
    ''', 
    '''
    +---+
    O   |
   /|\  |
   / \  |
       === 
    '''
]

# Mostrar as figuras do boneco na forca (linhas de teste):
'''
for i in range(7):
    print(FORCA[i],'\n')
'''

# Jogo para 1 jogador: usar palavras armazenadas no jogo
# Jogo para 2 jogadores: usar palavra definida pelo jogador 1.
palavras = 'melancia cadeira toalha banheiro ventilador avenida biologia'.split()

# print(palavras) # Linha de teste

# Obter palavra aleatória da lista
def palavraAleatoria(palavras):
    # retorna uma string aleatória de uma lista de strings
    indice = random.randint(0, len(palavras) - 1)
    return palavras[indice]

# print(palavraAleatoria(palavras)) # Linha de teste

# Mostrar tela da forca
def mostraForca(letrasErradas,letrasCorretas,palavra):
    print(FORCA[len(letrasErradas)])
    print()
    
    brancos = '_' * len(palavra)
    
    for i in range(len(palavra)):
        if (palavra[i] in letrasCorretas):
            brancos = brancos[:i] + palavra[i] + brancos[i+1:]
            
    for letra in brancos:
        print(letra, end=' ')
    print()

# Obter e mostrar a letra que o usuário digitou
def obterLetra(jaDigitada):
    while True:
        print('\nDigite uma letra:')
        letraTentativa = input()
        limpaTela()
        # Validar entrada do usuário
        letraTentativa = letraTentativa.lower()
        if len(letraTentativa) != 1:
            print('Digite apenas UMA letra!')
        elif letraTentativa in jaDigitada:
            print('Você já tentou essa letra. Escolha outra.')
        elif letraTentativa not in 'abcdefghijklmnopqrstuvwxyz':
            print('Digite apenas letras. Tente novamente.')
        else:
            return letraTentativa

# Função para limpar a tela
def limpaTela():
    os.system('cls' if os.name=='nt' else 'clear')

# Início do Jogo
limpaTela()
print('\t\t\tJOGO DA FORCA\n')
print('Adaptado por Fábio dos Reis - Bóson Treinamentos\n')
fimDeJogo = False

# Determinar numero de jogadores
print('Entre com número de jogadores: 1 ou 2')
numJogadores = int(input())
print('Jogadores selecionados: {0}'.format(numJogadores))

# Obter ou gerar palavra a adivinhar
letrasErradas = ''
letrasCorretas = ''
if (numJogadores == 1):
    palavra = palavraAleatoria(palavras)
elif (numJogadores == 2):
    print('Jogador 1, digite a palavra desejada:')
    palavra = input()
else:
    print('Número incorreto de jogadores.')
    
# print('Palavra escolhida:', palavra) # Linha de teste

# Iniciar efetivamente o jogo.
while True:
    mostraForca(letrasErradas,letrasCorretas,palavra)
    
    # Jogador entra com uma letra:
    tentativa = obterLetra(letrasCorretas + letrasErradas)
    limpaTela()
    if tentativa in palavra:
        letrasCorretas = letrasCorretas + tentativa
         
        # Verificar se jogador ganhou
        achouTodasLetras = True
        for i in range(len(palavra)):
            if palavra[i] not in letrasCorretas:
                achouTodasLetras = False
                break
        if achouTodasLetras:
            print('Parabéns, você venceu!')
            limpaTela()
            fimDeJogo = True
    else:
         letrasErradas = letrasErradas + tentativa
         
         # Verificar se jogador perdeu
         if len(letrasErradas) == len(FORCA) - 1:
             mostraForca(letrasErradas,letrasCorretas,palavra)
             print('Perdeu!')
             print('A palavra era {}'.format(palavra))
             fimDeJogo = True
         
    if fimDeJogo == True:
        limpaTela()
        break






