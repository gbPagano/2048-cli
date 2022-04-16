import random
import os
import numpy as np

def terminal():

    jogadas = 0    
    pontos = [0]  
       
    tabuleiro = novo_jogo()
    while True:
        if jogadas == 0:
            os.system('cls')
            print('Jogue com w a s d')
            print(f'jogadas: {jogadas}')
            print(f'pontos: {pontos[0]}')
            print_tabuleiro(tabuleiro)
            jogada = input()
            if jogada_player(tabuleiro,jogada,pontos):
                jogadas +=1
                aparecer_peca(tabuleiro)
        else:
            
            os.system('cls')
            print(f'jogadas: {jogadas}')
            print(f'pontos: {pontos[0]}')
            print_tabuleiro(tabuleiro)

            if not verificar_final(tabuleiro,pontos):
                print('fim')
                print(f'pontuação final: {pontos[0]} em {jogadas} jogadas')
                break
            jogada = input()
            if jogada_player(tabuleiro,jogada,pontos):
                jogadas +=1
                aparecer_peca(tabuleiro)   

def print_tabuleiro(tabuleiro):

    print(" ╭──────┬──────┬──────┬──────╮")
    for i in range(4):
        for j in range(4):
            if not tabuleiro[i][j] == 0:
                if tabuleiro[i][j] < 10:
                    if j == 0:
                        print(f" │   {tabuleiro[i][j]}  │ ",end="")
                    else:
                        print(f"  {tabuleiro[i][j]}  │ ",end="")
                elif tabuleiro[i][j] < 100:
                    if j == 0:
                        print(f" │  {tabuleiro[i][j]}  │ ",end="")
                    else:
                        print(f" {tabuleiro[i][j]}  │ ",end="")
                elif tabuleiro[i][j] < 1000:
                    if j == 0:
                        print(f" │  {tabuleiro[i][j]} │ ",end="")
                    else:
                        print(f" {tabuleiro[i][j]} │ ",end="")
                else:
                    if j == 0:
                        print(f" │ {tabuleiro[i][j]} │ ",end="")
                    else:
                        print(f"{tabuleiro[i][j]} │ ",end="")
            else:
                if j == 0:
                    print(f" │      │ ",end="")
                else:
                    print(f"     │ ",end="")
        print()
        if i == 3:
            print(" ╰──────┴──────┴──────┴──────╯")
        else:
            print(" ├──────┼──────┼──────┼──────┤")

def verificar_disponibilidade(t):

    disponiveis = []
    for i in range(4):
        for j in range(4):
            if t[i][j] == 0:
                disponiveis.append([i,j])

    if disponiveis == []: return False
    else: return disponiveis

def novo_jogo():
    global pontos
    pontos = 0
    tabuleiro = [            
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
            [0,0,0,0],
        ]
    tabuleiro = np.array(tabuleiro)
    for i in range(2):
        disponiveis = verificar_disponibilidade(tabuleiro)
        a = random.choice(disponiveis)
        variavel_controle = random.randint(1,10)
        if variavel_controle == 10:
            tabuleiro[a[0]][a[1]] = 4
        else:
            tabuleiro[a[0]][a[1]] = 2

    return tabuleiro

def aparecer_peca(tabuleiro):

    disponiveis = verificar_disponibilidade(tabuleiro)
    a = random.choice(disponiveis)
    variavel_controle = random.randint(1,10)
    if variavel_controle == 10:
        tabuleiro[a[0]][a[1]] = 4
        return True
    else:
        tabuleiro[a[0]][a[1]] = 2
        return True

    return False

def jogada_player(t,jogada,pontos):

    if jogada == "s":
        if not baixo(t,pontos): return False
    elif jogada == "w":
        if not cima(t,pontos): return False
    elif jogada == "d":
        if not direita(t,pontos): return False
    elif jogada == "a":
        if not esquerda(t,pontos): return False
    else:
        return False

    return True

def esquerda(t,pontos):

    movimentou = movimento(t,pontos)

    return movimentou

def direita(t,pontos):

    t = np.fliplr(t)
    movimentou = movimento(t,pontos)
    t = np.fliplr(t)

    return movimentou

def cima(t,pontos):

    t = np.rot90(t)
    movimentou = movimento(t,pontos)
    t = np.rot90(t,3)
            
    return movimentou

def baixo(t,pontos):

    t = np.flip(t)
    t = np.rot90(t)
    movimentou = movimento(t,pontos)
    t = np.rot90(t,3)
    t = np.flip(t)
            
    return movimentou

def verificar_final(t,pontos):

    if not verificar_disponibilidade(t):
    
        copia = np.copy(t)

        if esquerda(copia,pontos): return True
        elif cima(copia,pontos): return True
        elif direita(copia,pontos): return True
        elif baixo(copia,pontos): return True
        else: return False                  

    return True

def movimento(t,pontos):

    movimentou = mover(t)
    somou = somar(t,pontos)
    if somou:
        mover(t)

    if somou or movimentou: return True

    return False

def mover(t):
    movimentou = False

    for i in range(4):
        for j in range(4):
            if t[i][j] != 0:
                if j > 0 and t[i][j-1] == 0:
                    t[i][j-1] , t[i][j] = t[i][j] , 0
                    movimentou = True
                    if j > 1 and t[i][j-2] == 0:
                        t[i][j-2] , t[i][j-1] = t[i][j-1] , 0
                        if j > 2 and t[i][j-3] == 0:
                            t[i][j-3] , t[i][j-2] = t[i][j-2] , 0

    return movimentou

def somar(t,pontos):
    
    movimentou = False
    for i in range(4):
        for j in range(4):
            if t[i][j] != 0:
                if j > 0 and t[i][j-1] == t[i][j]:
                    pontos[0] += t[i][j]*2
                    t[i][j-1] , t[i][j] = t[i][j]*2 , 0
                    movimentou = True

    return movimentou

if __name__ == "__main__":
    terminal()