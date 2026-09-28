from random import randint

from constantes import *  

def gera_posicao_desocupada(posicoes_ocupadas, largura_mapa, altura_mapa):
    p = True

    while p:                                            
        x = randint(1, largura_mapa-2)
        y = randint(1, altura_mapa-2)
        posicao = [x, y]

        if posicao not in posicoes_ocupadas:
            posicoes_ocupadas.append(posicao)
            p = False

    return posicao


def gera_objetos(quantidade, tipo, cor, largura_mapa, altura_mapa, posicoes_ocupadas):
    objetos = []

    for i in range(quantidade):
        posicao = gera_posicao_desocupada(posicoes_ocupadas, largura_mapa, altura_mapa)
        objetos.append({
            'tipo': tipo,
            'posicao': posicao,
            'cor': cor,
        })

    return objetos


def inicializa_estado():
    posicoes_ocupadas = [] 

    # mapa com paredes já desenhadas importando do arquivo mapa.txt
    with open('mapa.txt', 'r') as arquivo:
        linhas = arquivo.read().splitlines()

    mapa = []
    paredes = []

    for y in range(len(linhas)):
        linha_mapa = []

        for x in range(len(linhas[y])):
            caractere = linhas[y][x]

            if caractere == '#':
                paredes.append([x, y])
                linha_mapa.append(' ')

            elif caractere == '.':
                linha_mapa.append(' ')

        mapa.append(linha_mapa)

    for parede in paredes:
        posicoes_ocupadas.append(parede)
    
    largura_mapa = len(mapa[0])
    altura_mapa = len(mapa)
    
    # define posição inicial do jogador
    pos_jogador = [largura_mapa//2, altura_mapa//2]  # Meio do mapa
    posicoes_ocupadas.append(pos_jogador)


    # cria objetos do mapa
    objetos = []
    objetos += gera_objetos(10, CORACAO, VERMELHO, largura_mapa, altura_mapa, posicoes_ocupadas)
    objetos += gera_objetos(10, ESPINHO, VERDE_CLARO, largura_mapa, altura_mapa, posicoes_ocupadas)

    for objeto in objetos:
        posicoes_ocupadas.append(objeto['posicao'])


    # cria monstros do mapa
    monstros = []
    monstros += gera_objetos(8, MONSTRO1, ROXO, largura_mapa, altura_mapa, posicoes_ocupadas)
    monstros += gera_objetos(7, MONSTRO2, ROXO, largura_mapa, altura_mapa, posicoes_ocupadas)
    monstros += gera_objetos(7, MONSTRO3, ROXO, largura_mapa, altura_mapa, posicoes_ocupadas)
    for monstro in monstros:
        monstro['vida_reduzida_martelo'] = False
        
        if monstro['tipo'] == MONSTRO1:
            monstro['vida'] = 5
            monstro['max_vidas'] = 5
            monstro['probabilidade de ataque'] = 0.20

        elif monstro['tipo'] == MONSTRO2:
            monstro['vida'] = 3
            monstro['max_vidas'] = 3
            monstro['probabilidade de ataque'] = 0.40
            monstro['eixo'] = None # definir direção do movimento do monstro - ver função de movimento dos monstros

        elif monstro['tipo'] == MONSTRO3:
            monstro['vida'] = 2
            monstro['max_vidas'] = 2
            monstro['probabilidade de ataque'] = 0.60
            monstro['situação'] = None # definir se está na rodada de o konstro andar ou não - ver função de movimento dos monstros

        posicoes_ocupadas.append(monstro['posicao'])


    # cria itens do mapa e inventário
    itens = []
    itens += gera_objetos(4, POCAO, COR_POCAO, largura_mapa, altura_mapa, posicoes_ocupadas)
    itens += gera_objetos(3, ELIXIR, COR_ELIXIR, largura_mapa, altura_mapa, posicoes_ocupadas)
    itens += gera_objetos(2, ESPADA, COR_ESPADA, largura_mapa, altura_mapa, posicoes_ocupadas)
    itens += gera_objetos(2, MARTELO, COR_MARTELO, largura_mapa, altura_mapa, posicoes_ocupadas)
    itens += gera_objetos(3, CHAVE, COR_CHAVE, largura_mapa, altura_mapa, posicoes_ocupadas)
    
    for iten in itens:
        posicoes_ocupadas.append(iten['posicao'])
        iten['status'] = None

    inventario = {'✦': 0, '⚗': 0, '†': 0, '⚒': 0, '⚿': 0}


    # define posição inicial do jogador na sala secreta
    pos_jogador_sala = [10, 10]


    # define posição das paredes, itens e objetos na sala (posições não aleatórias)
    paredes_sala = []
    altura_sala = 0
    largura_sala = 0

    objetos_sala = [
    {'tipo': CORACAO, 'posicao': [12, 6], 'cor': VERMELHO},
    {'tipo': CORACAO, 'posicao': [30, 5], 'cor': VERMELHO},
    {'tipo': CORACAO, 'posicao': [48, 7], 'cor': VERMELHO},
    {'tipo': CORACAO, 'posicao': [66, 5], 'cor': VERMELHO},
    {'tipo': CORACAO, 'posicao': [84, 7], 'cor': VERMELHO},
    {'tipo': CORACAO, 'posicao': [102, 6], 'cor': VERMELHO},
    {'tipo': CORACAO, 'posicao': [8, 14], 'cor': VERMELHO},
    {'tipo': CORACAO, 'posicao': [110, 14], 'cor': VERMELHO},
    {'tipo': CORACAO, 'posicao': [10, 22], 'cor': VERMELHO},
    {'tipo': CORACAO, 'posicao': [108, 22], 'cor': VERMELHO},
    {'tipo': CORACAO, 'posicao': [26, 24], 'cor': VERMELHO},
    {'tipo': CORACAO, 'posicao': [46, 22], 'cor': VERMELHO},
    {'tipo': CORACAO, 'posicao': [64, 24], 'cor': VERMELHO},
    {'tipo': CORACAO, 'posicao': [82, 22], 'cor': VERMELHO},
    {'tipo': CORACAO, 'posicao': [100, 24], 'cor': VERMELHO}]

    itens_sala = [
        {'tipo': POCAO, 'posicao': [20, 10], 'cor': COR_POCAO, 'status': None},
        {'tipo': POCAO, 'posicao': [38, 9], 'cor': COR_POCAO, 'status': None},
        {'tipo': POCAO, 'posicao': [56, 12], 'cor': COR_POCAO, 'status': None},
        {'tipo': POCAO, 'posicao': [74, 9], 'cor': COR_POCAO, 'status': None},
        {'tipo': POCAO, 'posicao': [92, 11], 'cor': COR_POCAO, 'status': None},
        {'tipo': POCAO, 'posicao': [104, 17], 'cor': COR_POCAO, 'status': None},
        {'tipo': POCAO, 'posicao': [88, 18], 'cor': COR_POCAO, 'status': None},
        {'tipo': POCAO, 'posicao': [24, 18], 'cor': COR_POCAO, 'status': None},

        {'tipo': ELIXIR, 'posicao': [16, 16], 'cor': COR_ELIXIR, 'status': None},
        {'tipo': ELIXIR, 'posicao': [34, 14], 'cor': COR_ELIXIR, 'status': None},
        {'tipo': ELIXIR, 'posicao': [52, 17], 'cor': COR_ELIXIR, 'status': None},
        {'tipo': ELIXIR, 'posicao': [70, 14], 'cor': COR_ELIXIR, 'status': None},
        {'tipo': ELIXIR, 'posicao': [88, 15], 'cor': COR_ELIXIR, 'status': None},
        {'tipo': ELIXIR, 'posicao': [100, 20], 'cor': COR_ELIXIR, 'status': None},
        {'tipo': ELIXIR, 'posicao': [76, 20], 'cor': COR_ELIXIR, 'status': None},
        {'tipo': ELIXIR, 'posicao': [42, 20], 'cor': COR_ELIXIR, 'status': None},

        {'tipo': ESPADA, 'posicao': [22, 14], 'cor': COR_ESPADA, 'status': None},
        {'tipo': ESPADA, 'posicao': [40, 12], 'cor': COR_ESPADA, 'status': None},
        {'tipo': ESPADA, 'posicao': [58, 15], 'cor': COR_ESPADA, 'status': None},
        {'tipo': ESPADA, 'posicao': [78, 12], 'cor': COR_ESPADA, 'status': None},
        {'tipo': ESPADA, 'posicao': [96, 14], 'cor': COR_ESPADA, 'status': None},
        {'tipo': ESPADA, 'posicao': [90, 21], 'cor': COR_ESPADA, 'status': None},
        {'tipo': ESPADA, 'posicao': [60, 21], 'cor': COR_ESPADA, 'status': None},
        {'tipo': ESPADA, 'posicao': [32, 21], 'cor': COR_ESPADA, 'status': None},

        {'tipo': MARTELO, 'posicao': [18, 20], 'cor': COR_MARTELO, 'status': None},
        {'tipo': MARTELO, 'posicao': [28, 16], 'cor': COR_MARTELO, 'status': None},
        {'tipo': MARTELO, 'posicao': [46, 14], 'cor': COR_MARTELO, 'status': None},
        {'tipo': MARTELO, 'posicao': [62, 10], 'cor': COR_MARTELO, 'status': None},
        {'tipo': MARTELO, 'posicao': [80, 17], 'cor': COR_MARTELO, 'status': None},
        {'tipo': MARTELO, 'posicao': [98, 18], 'cor': COR_MARTELO, 'status': None},
        {'tipo': MARTELO, 'posicao': [70, 23], 'cor': COR_MARTELO, 'status': None},
        {'tipo': MARTELO, 'posicao': [50, 23], 'cor': COR_MARTELO, 'status': None}]


    # reúne todas as informações no estado inicial do jogo
    return {
        'tela_atual': TELA_INICIAL,
        'pos_jogador': pos_jogador,
        'pos_jogador_sala': pos_jogador_sala,
        'vidas': 5,  
        'max_vidas': 5,
        'experiencia': 0,
        'max_experiencia': 10,
        'nivel': 0,  
        'objetos': objetos,
        'objetos_sala': objetos_sala,
        'itens_sala': itens_sala,
        'paredes': paredes,
        'paredes_sala': paredes_sala,
        'altura_sala': altura_sala,
        'largura_sala': largura_sala,
        'monstros': monstros,
        'itens': itens,
        'mapa': mapa,
        'inventario': inventario,
        'equipamento': None,
        'mensagem': ''
    }


inicializa_estado()