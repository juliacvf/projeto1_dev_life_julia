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

def cria_mapa():
    with open('mapa.txt', 'r') as arquivo:
        mapa = arquivo.read().splitlines()


def inicializa_estado():
    posicoes_ocupadas = []

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
        
    print(mapa)

    for parede in paredes:
        posicoes_ocupadas.append(parede)
        
    
    largura_mapa = len(mapa[0])
    altura_mapa = len(mapa)
    
    
    pos_jogador = [largura_mapa//2, altura_mapa//2]  # Meio do mapa
    
    
    # Cria outros objetos do mapa
    posicoes_ocupadas.append(pos_jogador)

    objetos = []
    objetos += gera_objetos(10, CORACAO, VERMELHO, largura_mapa, altura_mapa, posicoes_ocupadas)
    objetos += gera_objetos(12, ESPINHO, VERDE_CLARO, largura_mapa, altura_mapa, posicoes_ocupadas)

    for objeto in objetos:
        posicoes_ocupadas.append(objeto['posicao'])

    monstros = []
    monstros += gera_objetos(7, MONSTRO1, ROXO, largura_mapa, altura_mapa, posicoes_ocupadas)
    monstros += gera_objetos(4, MONSTRO2, ROXO, largura_mapa, altura_mapa, posicoes_ocupadas)
    monstros += gera_objetos(3, MONSTRO3, ROXO, largura_mapa, altura_mapa, posicoes_ocupadas)
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
        'mensagem': '', # Use esta mensagem para mostrar mensagens ao jogador, como "Você perdeu uma vida" ou "Você ganhou uma vida"
    }


inicializa_estado()  # Chame a função para inicializar o estado do jogo