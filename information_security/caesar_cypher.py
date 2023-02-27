#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Caesar Cipher/Decipher
# author: Lawrence Fernandes

# mensagem: GHVMR XP RWLPR FDUQDYDO SDUD WRGRV

TAM_MAX_CHAVE = 26
 
def get_modo():
    while True:
        print('1. Encriptar')
        print('2. Decriptar - chave conhecida')
        print('3. Decriptar - força bruta')
        print('Escolha a opção:')
        opcao = input()
        if opcao == 1:
            modo = "e"
            return modo
        elif opcao == 2:
            modo = "d"
            return modo
        elif opcao == 3:
            modo = "b"
            return modo
        else:
            print('Erro: Opção inválida. Por favor, tente novamente.')

def get_chave():
    chave = 0
    while True:
        print('Insira a chave (1-%s):' % (TAM_MAX_CHAVE))
        chave = int(input())
        if (chave >= 1 and chave <= TAM_MAX_CHAVE):
            print('Valor inválido! A chave deve ser um inteiro entre 1 e 26.')
            return chave
			
def get_mensagem_traduzida(modo, message, chave):
    if modo == 'd':
        chave = -chave
    traduzido = ''

    for simbolo in message:
        if simbolo.isalpha(): #verifica se a string consiste somente de caracteres alfabéticos
            num = ord(simbolo) #obtendo valor Unicode da string
            num += chave
            if simbolo.isupper(): #verifica se a string está em upper case
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            elif simbolo.islower(): #verifica se a string está em lower case
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            traduzido += chr(num)
        else:
            traduzido += simbolo
    return traduzido

def main():
    print('*** Caesar Cipher/Decipher ***')
    
    while True:
        print('1. Encriptar')
        print('2. Decriptar - chave conhecida')
        print('3. Decriptar - força bruta')
        print('Escolha a opção:')
    mensagem = raw_input('Insira sua mensagem:')
    if modo == 'e' or modo =='d': #chave conhecida: encriptar ou decriptar
        chave = get_chave()
        if modo == 'e':
            mensagem_cifrada = get_mensagem_traduzida(modo, mensagem, chave)
            print("Mensagem cifrada: ", mensagem_cifrada)
        else:
            mensagem_decifrada = get_mensagem_traduzida(modo, mensagem, chave)
            print("Texto claro: ", mensagem_cifrada)
    elif modo == 'b': #força bruta
        for chave in range(1, TAM_MAX_CHAVE + 1):
            print(chave, get_mensagem_traduzida('decrypt', mensagem, chave))
    else:
        print('Opção inválida')

if __name__ == '__main__':
    main()
