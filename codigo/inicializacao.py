from random import randint

from constantes import *  # Você pode usar as constantes definidas em constantes.py, se achar útil
                          # Por exemplo, usar a constante CORACAO é o mesmo que colocar a string '❤'
                          # diretamente no código


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
    """
    Esta função já está pronta, você não precisa modificá-la.

    Gera uma lista de objetos do tipo especificado, com a quantidade especificada.
    Cada objeto é um dicionário com as chaves 'tipo', 'posicao' e 'cor'.

    Parâmetros:
    quantidade: quantidade de objetos a serem gerados
    tipo: tipo do objeto a ser gerado. É uma string como '❤'
    cor: cor do objeto a ser gerado. É uma lista com três elementos, como [255, 0, 0]
    largura_mapa: largura do mapa do jogo em caracteres
    altura_mapa: altura do mapa do jogo em caracteres
    posicoes_ocupadas: lista de posições ocupadas no mapa. Cada posição é uma lista com exatamente dois elementos: a posição x e a posição y.
    """
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

    mapa = [
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
        [' '] * 50,
    ]
    

    paredes = [
    # Sala superior esquerda — teto
    [2, 1], [3, 1], [4, 1], [5, 1], [6, 1],
    [7, 1], [8, 1], [9, 1], [10, 1], [11, 1],
    [12, 1], [13, 1], [14, 1], [15, 1],

    # Sala superior esquerda — laterais
    [2, 2], [2, 3], [2, 4], [2, 5],
    [15, 2], [15, 3], [15, 5],

    # Sala superior esquerda — parte inferior com entradas
    [2, 6], [3, 6], [4, 6], [5, 6],
    [7, 6], [8, 6], [9, 6], [10, 6],
    [12, 6], [13, 6], [14, 6], [15, 6],

    # Divisões internas da sala superior esquerda
    [7, 2], [7, 3], [7, 5],
    [11, 3], [12, 3], [13, 3], [14, 3],

    # Sala superior central — teto
    [19, 1], [20, 1], [21, 1], [22, 1], [23, 1],
    [24, 1], [25, 1], [26, 1], [27, 1], [28, 1],
    [29, 1], [30, 1], [31, 1],

    # Sala superior central — laterais
    [19, 2], [19, 3], [19, 5],
    [31, 2], [31, 4], [31, 5],

    # Sala superior central — parte inferior
    [19, 6], [20, 6], [21, 6], [22, 6],
    [24, 6],
    [27, 6], [28, 6], [29, 6], [30, 6], [31, 6],

    # Divisões internas da sala superior central
    [23, 2], [23, 3], [23, 4],
    [27, 3], [28, 3], [29, 3], [30, 3],

    # Sala superior direita — teto
    [35, 1], [36, 1], [37, 1], [38, 1], [39, 1],
    [40, 1], [41, 1], [42, 1], [43, 1], [44, 1],
    [45, 1], [46, 1], [47, 1],

    # Sala superior direita — laterais
    [35, 2], [35, 4], [35, 5],
    [47, 2], [47, 3], [47, 4], [47, 5],

    # Sala superior direita — parte inferior
    [35, 6], [36, 6], [37, 6],
    [39, 6], [40, 6], [41, 6], [42, 6],
    [44, 6], [45, 6], [46, 6], [47, 6],

    # Divisões internas da sala superior direita
    [39, 2], [39, 3], [39, 4],
    [43, 3], [44, 3], [45, 3], [46, 3],

    # Corredores centrais
    [4, 8], [5, 8], [6, 8], [7, 8], [8, 8],
    [10, 8], [11, 8], [12, 8], [13, 8],

    [16, 7], [16, 8], [16, 9],

    [19, 8], [20, 8], [21, 8], [22, 8],
    [28, 8], [29, 8], [30, 8], [31, 8],

    [34, 7], [34, 8], [34, 9],

    [37, 8], [38, 8], [39, 8], [40, 8],
    [42, 8], [43, 8], [44, 8], [45, 8],

    # Sala inferior esquerda — teto
    [2, 10], [3, 10], [4, 10], [5, 10],
    [7, 10], [8, 10], [9, 10], [10, 10],
    [11, 10], [12, 10], [13, 10], [14, 10],

    # Sala inferior esquerda — laterais
    [2, 11], [2, 12], [2, 13],
    [14, 11], [14, 13],

    # Sala inferior esquerda — chão
    [2, 13], [3, 13], [4, 13], [5, 13], [6, 13],
    [7, 13], [8, 13],
    [10, 13], [11, 13], [12, 13], [13, 13], [14, 13],

    # Divisões internas da sala inferior esquerda
    [6, 11], [6, 12],
    [10, 11], [11, 11], [12, 11], [13, 11],

    # Sala inferior central — teto
    [18, 10], [19, 10], [20, 10], [21, 10],
    [23, 10], [24, 10], [25, 10], [26, 10],
    [27, 10], [28, 10], [29, 10], [30, 10], [31, 10],

    # Sala inferior central — laterais
    [18, 11], [18, 13],
    [31, 11], [31, 12], [31, 13],

    # Sala inferior central — chão
    [18, 13], [19, 13], [20, 13], [21, 13], [22, 13],
    [24, 13], [25, 13], [26, 13], [27, 13],
    [28, 13], [29, 13], [30, 13], [31, 13],

    # Divisões internas da sala inferior central
    [22, 11], [22, 12],
    [27, 11], [28, 11], [29, 11], [30, 11],

    # Sala inferior direita — teto
    [35, 10], [36, 10], [37, 10], [38, 10],
    [39, 10], [40, 10],
    [42, 10], [43, 10], [44, 10], [45, 10],
    [46, 10], [47, 10],

    # Sala inferior direita — laterais
    [35, 11], [35, 12], [35, 13],
    [47, 11], [47, 13],

    # Sala inferior direita — chão
    [35, 13], [36, 13], [37, 13], [38, 13],
    [40, 13], [41, 13], [42, 13], [43, 13],
    [44, 13], [45, 13], [46, 13], [47, 13],

    # Divisões internas da sala inferior direita
    [39, 11], [39, 12],
    [43, 11], [44, 11], [45, 11], [46, 11],
]

    
    for parede in paredes:
        posicoes_ocupadas.append(parede)
        
    
    largura_mapa = len(mapa[0])
    altura_mapa = len(mapa)
    
    # Você pode colocar o jogador em outro lugar, se preferir
    pos_jogador = [largura_mapa//2, altura_mapa//2]  # Meio do mapa
    
    
    # Cria outros objetos do mapa
    posicoes_ocupadas.append(pos_jogador)

    objetos = []
    objetos += gera_objetos(8, CORACAO, VERMELHO, largura_mapa, altura_mapa, posicoes_ocupadas)
    objetos += gera_objetos(6, ESPINHO, VERDE_CLARO, largura_mapa, altura_mapa, posicoes_ocupadas)

    for objeto in objetos:
        posicoes_ocupadas.append(objeto['posicao'])

    monstros = []
    monstros += gera_objetos(2, MONSTRO1, ROXO, largura_mapa, altura_mapa, posicoes_ocupadas)
    monstros += gera_objetos(3, MONSTRO2, ROXO, largura_mapa, altura_mapa, posicoes_ocupadas)
    monstros += gera_objetos(2, MONSTRO3, ROXO, largura_mapa, altura_mapa, posicoes_ocupadas)
    for monstro in monstros:
        if monstro['tipo'] == MONSTRO1:
            monstro['vida'] = 5
            monstro['probabilidade de ataque'] = 0.2

        elif monstro['tipo'] == MONSTRO2:
            monstro['vida'] = 3
            monstro['probabilidade de ataque'] = 0.4
            monstro['eixo'] = None
    

        elif monstro['tipo'] == MONSTRO3:
            monstro['vida'] = 2
            monstro['probabilidade de ataque'] = 0.6
            monstro['situação'] = None

    print(monstros)

    return {
        'tela_atual': TELA_INICIAL,
        'pos_jogador': pos_jogador,
        'vidas': 5,  
        'max_vidas': 5,
        'experiencia': 0,
        'max_experiencia': 10,
        'nivel': 0,  
        'objetos': objetos,
        'paredes': paredes,
        'monstros': monstros,
        'mapa': mapa,
        'mensagem': '',  # Use esta mensagem para mostrar mensagens ao jogador, como "Você perdeu uma vida" ou "Você ganhou uma vida"
    }


inicializa_estado()  # Chame a função para inicializar o estado do jogo