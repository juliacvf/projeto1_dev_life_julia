# arquivo com as funções auxiliares criadas para dar mais fluidez à construção do código

from constantes import *
import motor_grafico as motor
import random
from inicializacao import gera_objetos



def movimento_dos_monstros(estado, tecla, posicao_inicial_jogador): # definição das movimentações dos monstros 
    movimentos = [motor.SETA_ESQUERDA, motor.SETA_DIREITA, motor.SETA_CIMA, motor.SETA_BAIXO]
    mapa = estado['mapa']
    monstros = estado['monstros']
    posicao_monstros = []
    
    for monstro in monstros:
        posicao_monstros.append(monstro['posicao'])

    posicao_objetos = []
    for objeto in estado['objetos']:
        if objeto['tipo'] == ESPINHO:
            posicao_objetos.append(objeto['posicao'])

    x = posicao_inicial_jogador[0]
    y = posicao_inicial_jogador[1]

    for monstro in monstros:
        xm = monstro['posicao'][0]
        ym = monstro['posicao'][1]

        # determinação de que movimento dos monstro só ocorre mediante movimentação do jogador e apenas se o jogador ñ estiver se movimentado para sua posição
        if (tecla == motor.SETA_ESQUERDA and [x-1, y] != [xm, ym]) or (tecla == motor.SETA_DIREITA and [x+1, y] != [xm, ym]) or (tecla == motor.SETA_CIMA and [x, y-1] != [xm, ym]) or (tecla == motor.SETA_BAIXO and [x, y+1] != [xm, ym]):

            # movimentação p/ monstro do tipo 1
            if monstro['tipo'] == MONSTRO1:
                movimento = random.choice(movimentos) # movimento determinado por sorteio da direção

                # movimento ocorre apenas se ñ for empedido por paredes, outros monstros ou objetos
                if movimento == motor.SETA_ESQUERDA and [xm-1, ym] not in estado['paredes'] and [xm-1, ym] not in posicao_monstros and [xm-1, ym] not in posicao_objetos and [xm-1, ym] != estado['pos_jogador'] and xm-1 >= 0:
                    xm -= 1
                elif movimento == motor.SETA_DIREITA and [xm+1, ym] not in estado['paredes'] and [xm+1, ym] not in posicao_monstros and [xm+1, ym] not in posicao_objetos and [xm+1, ym] != estado['pos_jogador'] and xm+1 < len(mapa[0]):
                    xm += 1
                elif movimento == motor.SETA_CIMA and [xm, ym-1] not in estado['paredes'] and [xm, ym-1] not in posicao_monstros and [xm, ym-1] not in posicao_objetos and [xm, ym-1] != estado['pos_jogador'] and ym-1 >= 0:
                    ym -= 1
                elif movimento == motor.SETA_BAIXO and [xm, ym+1] not in estado['paredes'] and [xm, ym+1] not in posicao_monstros and [xm, ym+1] not in posicao_objetos and [xm, ym+1] != estado['pos_jogador'] and ym+1 < len(mapa):
                    ym += 1

            # movimentação p/ monstro do tipo 2
            elif monstro['tipo'] == MONSTRO2: # movimentação em um estilo de perseguição
                distancia_horizontal = abs(xm - estado['pos_jogador'][0])
                distancia_vertical = abs(ym - estado['pos_jogador'][1])

                if monstro['eixo'] == None: # o primeiro movimento será determinado pela maior distancia entre os eixos horizontal e vertical do jogador ao monstro
                    if distancia_horizontal > distancia_vertical:
                        if estado['pos_jogador'][0] - xm < 0 and [xm-1, ym] not in estado['paredes'] and [xm-1, ym] not in posicao_monstros and [xm-1, ym] not in posicao_objetos and [xm-1, ym] != estado['pos_jogador'] and xm-1 >= 0:
                            xm -= 1
                            monstro['eixo'] = 'vertical'
                        elif estado['pos_jogador'][0] - xm > 0 and  [xm+1, ym] not in estado['paredes'] and [xm+1, ym] not in posicao_monstros and [xm+1, ym] not in posicao_objetos and [xm+1, ym] != estado['pos_jogador'] and xm+1 < len(mapa[0]):
                            xm += 1
                            monstro['eixo'] = 'vertical'
                        else:
                            monstro['eixo'] = 'vertical' # o movimento seguinte sempre será na outra direção possível, mesmo que devido algum empedimento físico o monstro ñ tenha conseguido se mover na direção da vez 

                    else:
                        if estado['pos_jogador'][1] - ym < 0 and [xm, ym-1] not in estado['paredes'] and [xm, ym-1] not in posicao_monstros and [xm, ym-1] not in posicao_objetos and [xm, ym-1] != estado['pos_jogador'] and ym-1 >= 0:
                            ym -= 1
                            monstro['eixo'] = 'horizontal'
                        elif estado['pos_jogador'][1] - ym > 0 and [xm, ym+1] not in estado['paredes'] and [xm, ym+1] not in posicao_monstros and [xm, ym+1] not in posicao_objetos and [xm, ym+1] != estado['pos_jogador'] and ym+1 < len(mapa):
                            ym += 1
                            monstro['eixo'] = 'horizontal'
                        else:
                            monstro['eixo'] = 'horizontal'

                elif monstro['eixo'] == 'vertical':
                    if estado['pos_jogador'][1] - ym < 0 and [xm, ym-1] not in estado['paredes'] and [xm, ym-1] not in posicao_monstros and [xm, ym-1] not in posicao_objetos and [xm, ym-1] != estado['pos_jogador'] and ym-1 >= 0:
                        ym -= 1
                        monstro['eixo'] = 'horizontal'
                    elif estado['pos_jogador'][1] - ym > 0 and [xm, ym+1] not in estado['paredes'] and [xm, ym+1] not in posicao_monstros and [xm, ym+1] not in posicao_objetos and [xm, ym+1] != estado['pos_jogador'] and ym+1 < len(mapa):
                        ym += 1
                        monstro['eixo'] = 'horizontal'
                    else:
                        monstro['eixo'] = 'horizontal'

                elif monstro['eixo'] == 'horizontal':
                    if estado['pos_jogador'][0] - xm < 0 and [xm-1, ym] not in estado['paredes'] and [xm-1, ym] not in posicao_monstros and [xm-1, ym] not in posicao_objetos and [xm-1, ym] != estado['pos_jogador'] and xm-1 >= 0:
                        xm -= 1
                        monstro['eixo'] = 'vertical'
                    elif estado['pos_jogador'][0] - xm > 0 and  [xm+1, ym] not in estado['paredes'] and [xm+1, ym] not in posicao_monstros and [xm+1, ym] not in posicao_objetos and [xm+1, ym] != estado['pos_jogador'] and xm+1 < len(mapa[0]):
                        xm += 1
                        monstro['eixo'] = 'vertical'
                    else:
                        monstro['eixo'] = 'vertical'
                    
            # movimentação do monstro tipo 3
            elif monstro['tipo'] == MONSTRO3: # movimentação também em estilo de perseguição
                distancia_horizontal = abs(xm - estado['pos_jogador'][0])
                distancia_vertical = abs(ym - estado['pos_jogador'][1])
                distancias = ['horizontal', 'vertical']
                situacao = ['esperar', 'avançar'] # o monstro não se move em todas as jogadas. A cada duas jogadas sua movimentação é ativada, sendo feita de duas em duas casas

                if monstro['situação'] == None:
                    situação = random.choice(situacao)
                    monstro['situação'] = situação

                if monstro['situação'] == 'avançar': # quando está em sua vez de avançar, o monstro verifica em qual direção ele se encontra mais distante do jogador, sempre executando seu movimento nessa direção, objetivando o encurtamento dessa distancia andando para o sentido mais próximo ao jogador
                    if distancia_horizontal > distancia_vertical: 
                        if estado['pos_jogador'][0] - xm < 0 and [xm-1, ym] not in estado['paredes'] and [xm-1, ym] not in posicao_monstros and [xm-1, ym] not in posicao_objetos and [xm-1, ym] != estado['pos_jogador'] and [xm-2, ym] not in estado['paredes'] and [xm-2, ym] not in posicao_monstros and [xm-2, ym] not in posicao_objetos and [xm-2, ym] != estado['pos_jogador'] and xm-2 >= 0:
                            xm -= 2
                        elif estado['pos_jogador'][0] - xm > 0 and [xm+1, ym] not in estado['paredes'] and [xm+1, ym] not in posicao_monstros and [xm+1, ym] not in posicao_objetos and [xm+1, ym] != estado['pos_jogador'] and [xm+2, ym] not in estado['paredes'] and [xm+2, ym] not in posicao_monstros and [xm+2, ym] not in posicao_objetos and [xm+2, ym] != estado['pos_jogador'] and xm+2 < len(mapa[0]):
                            xm += 2
                    elif distancia_vertical > distancia_horizontal:
                        if estado['pos_jogador'][1] - ym < 0 and [xm, ym-1] not in estado['paredes'] and [xm, ym-1] not in posicao_monstros and [xm, ym-1] not in posicao_objetos and [xm, ym-1] != estado['pos_jogador'] and [xm, ym-2] not in estado['paredes'] and [xm, ym-2] not in posicao_monstros and [xm, ym-2] not in posicao_objetos and [xm, ym-2] != estado['pos_jogador'] and ym-2 >= 0:
                            ym -= 2
                        elif estado['pos_jogador'][1] - ym > 0 and [xm, ym+1] not in estado['paredes'] and [xm, ym+1] not in posicao_monstros and [xm, ym+1] not in posicao_objetos and [xm, ym+1] != estado['pos_jogador'] and [xm, ym+2] not in estado['paredes'] and [xm, ym+2] not in posicao_monstros and [xm, ym+2] not in posicao_objetos and [xm, ym+2] != estado['pos_jogador'] and ym+2 < len(mapa):
                            ym += 2
                    else:
                        distancia = random.choice(distancias) # se as distancias em ambas direções são as mesmas, ele sorteia a direção de seu movimento e anda nessa rumando o sentido em que está mais próximo do jogador 
                        if distancia == 'horizontal':
                            if estado['pos_jogador'][0] - xm < 0 and [xm-1, ym] not in estado['paredes'] and [xm-1, ym] not in posicao_monstros and [xm-1, ym] not in posicao_objetos and [xm-1, ym] != estado['pos_jogador'] and [xm-2, ym] not in estado['paredes'] and [xm-2, ym] not in posicao_monstros and [xm-2, ym] not in posicao_objetos and [xm-2, ym] != estado['pos_jogador'] and xm-2 >= 0:
                                xm -= 2
                            elif estado['pos_jogador'][0] - xm > 0 and [xm+1, ym] not in estado['paredes'] and [xm+1, ym] not in posicao_monstros and [xm+1, ym] not in posicao_objetos and [xm+1, ym] != estado['pos_jogador'] and [xm+2, ym] not in estado['paredes'] and [xm+2, ym] not in posicao_monstros and [xm+2, ym] not in posicao_objetos and [xm+2, ym] != estado['pos_jogador'] and xm+2 < len(mapa[0]):
                                xm += 2
                        else:
                            if estado['pos_jogador'][1] - ym < 0 and [xm, ym-1] not in estado['paredes'] and [xm, ym-1] not in posicao_monstros and [xm, ym-1] not in posicao_objetos and [xm, ym-1] != estado['pos_jogador'] and [xm, ym-2] not in estado['paredes'] and [xm, ym-2] not in posicao_monstros and [xm, ym-2] not in posicao_objetos and [xm, ym-2] != estado['pos_jogador'] and ym-2 >= 0:
                                ym -= 2
                            elif estado['pos_jogador'][1] - ym > 0 and [xm, ym+1] not in estado['paredes'] and [xm, ym+1] not in posicao_monstros and [xm, ym+1] not in posicao_objetos and [xm, ym+1] != estado['pos_jogador'] and [xm, ym+2] not in estado['paredes'] and [xm, ym+2] not in posicao_monstros and [xm, ym+2] not in posicao_objetos and [xm, ym+2] != estado['pos_jogador'] and ym+2 < len(mapa):
                                ym += 2
                    monstro['situação'] = 'esperar'

                elif monstro['situação'] == 'esperar':
                    monstro['situação'] = 'avançar'


        # a cada movimento dos monstros, a função de estado contendo os dicionarios com as informações dos monstros é atualizada em sua chave posições 
        if [xm, ym] != monstro['posicao']:
            posicao_monstros.remove(monstro['posicao'])
            monstro['posicao'] = [xm, ym]
            posicao_monstros.append(monstro['posicao']) # a lista com posições dos monstros também é atualizada 

def atualizacao_inventario(estado, tecla): # definição dos comandos de uso de itens e atalizações de estado a depender do resultado 
    if tecla == 'p':
        if estado['inventario']['⚗'] >= 1:
            estado['inventario']['⚗'] -= 1
            numero = random.random() # sorteio de numero entre 0 e 1 p/ ver se o uso da poção adicionara ou retirará uma vida do total de vidas do jogador 
            if numero <= 0.4:  # 40% de chance de perder uma vida
                estado['vidas'] -= 1
                estado['max_vidas'] -= 1
                if estado['vidas'] <= 0:
                    estado['vidas'] = 0
                    estado['mensagem'] = 'Você perdeu todas as vidas'
                    estado['tela_atual'] = TELA_GAME_OVER
                else:
                    estado['mensagem'] = 'Sua quantidade máxima de vidas diminuiu'
            else:
                estado['max_vidas'] += 1
                estado['vidas'] += 1
                estado['mensagem'] = 'Sua quantidade máxima de vidas aumentou' # 60% de chance de ganhar uma vida
        else:
            estado['mensagem'] = 'Você não tem poções' # caso não haja poções no inventário


    elif tecla == 'e':
        if estado['inventario']['✦'] >= 1:
            estado['inventario']['✦'] -= 1
            estado['experiencia'] += 2 # o uso do elixir adiciona 2 pontos de experiência para o jogador 
            estado['mensagem'] = 'Você ganhou 2 pontos de experiência'
        else:
            estado['mensagem'] = 'Você não tem elixir' # caso não haja elixir no inventário


    elif tecla == 's':
        if estado['equipamento'] is None: # se a espada não estiver equipada e não houver nenhum outro item equipado, ao apertar s a espada será equipada
            if estado['inventario']['†'] >= 1:
                estado['inventario']['†'] -= 1
                estado['equipamento'] = 'espada'
                estado['mensagem'] = 'Espada equipada'
                for monstro in estado['monstros']: # com a espada equipada, a chance de o jogador ganahr batalhas contra todos os monstros será aumentada 
                    if monstro['tipo'] == MONSTRO1:
                        monstro['probabilidade de ataque'] = 0.15 # reduz de 20% p/ 15%

                    elif monstro['tipo'] == MONSTRO2:
                        monstro['probabilidade de ataque'] = 0.35 # reduz de 40% p/ 35%

                    elif monstro['tipo'] == MONSTRO3:
                        monstro['probabilidade de ataque'] = 0.50 # reduz de 60% p/ 50%
            else:
                estado['mensagem'] = 'Você não tem espada para equipar' # caso não haja espada no inventário

        elif estado['equipamento'] == 'espada': # se a espada estiver equipada, ao apertar s a espada será desequipada
            estado['equipamento'] = None
            estado['mensagem'] = 'Espada desequipada'
            # a ideia é que itens desequipados sejam descartados para manter uma maior fluidez no jogo e, por isso, o estado do inventário não é reatualizado após desequipamento da espada

            for monstro in estado['monstros']: # retorno das chances de batalha ao estado original
                if monstro['tipo'] == MONSTRO1:
                    monstro['probabilidade de ataque'] = 0.20 

                elif monstro['tipo'] == MONSTRO2:
                    monstro['probabilidade de ataque'] = 0.40

                elif monstro['tipo'] == MONSTRO3:
                    monstro['probabilidade de ataque'] = 0.60

        else:
            estado['mensagem'] = 'Você já possui outro item equipado' # se a espada não estiver equipada e já houver um outro item equipado, não será possível equipar a espada antes de desequipar o outro item

        
    elif tecla == 'h': # construção semelhante à da espada, com diferenciação apenas na funcionalidade de uso
        if estado['equipamento'] is None:
            if estado['inventario']['⚒'] >= 1:
                estado['inventario']['⚒'] -= 1
                estado['equipamento'] = 'martelo'
                estado['mensagem'] = 'Martelo equipado'

                for monstro in estado['monstros']: # com o martelo equipado, as vidas máximas dos monstros são diminuidas em 1 unidade
                    if monstro['tipo'] == MONSTRO1:
                        monstro['max_vidas'] = 4 # diminuição de 5 p/ 4

                    elif monstro['tipo'] == MONSTRO2:
                        monstro['max_vidas'] = 2 # diminuição de 3 p/ 2

                    elif monstro['tipo'] == MONSTRO3:
                        monstro['max_vidas'] = 1 # diminuição de 2 p/ 1

                    if monstro['vida'] > monstro['max_vidas']: 
                        monstro['vida'] = monstro['max_vidas']

            else:
                estado['mensagem'] = 'Você não tem martelo para equipar' # caso não haja martelo no inventário

        elif estado['equipamento'] == 'martelo':
            estado['equipamento'] = None
            estado['mensagem'] = 'Martelo desequipado'

            for monstro in estado['monstros']:  # retorno das vidas máximas ao estado original
                if monstro['tipo'] == MONSTRO1:
                    monstro['max_vidas'] = 5

                elif monstro['tipo'] == MONSTRO2:
                    monstro['max_vidas'] = 3

                elif monstro['tipo'] == MONSTRO3:
                    monstro['max_vidas'] = 2
        else:
            estado['mensagem'] = 'Você já possui outro item equipado'
        
    elif tecla == 'k': # as chaves permitem o acesso à sala secreta a partir do pressionamento da tecla k. Para acessar a sala secreta é necessário o acumulo de 3 chaves, que serão descartadas depois do acesso
        if estado['inventario']['⚿'] < 3:  
            estado['mensagem'] = 'Você ainda não pode acessar a sala secreta'
        else: 
            estado['inventario']['⚿'] -= 3
            estado['tela_atual'] = TELA_SALA_SECRETA

def batalha(estado, monstro, posicao_monstros, posicoes_ocupadas, monstros): # definição do mecanismo de batalha com monstros
    numero = random.random() # sorteio de número entre 0 e 1 para verificação de ataque de jogador ou monstro
    if numero <= monstro['probabilidade de ataque']:
        estado['mensagem'] = "O monstro atacou e você perdeu uma vida"
        estado['vidas'] -= 1
        if estado['vidas'] == 0:
            estado['tela_atual'] = TELA_GAME_OVER # em caso de ataque do monstro, jogador perde uma vida e, caso suas vidas sejam zeradas, tela de game over abre e jogo podera ser reiniciado

    else:
        monstro['vida'] -= 1 # em caso de ataque do jogador, o monstro perde vidas
        if monstro['vida'] == 0:
            monstros.remove(monstro)
            posicao_monstros.remove(monstro['posicao'])
            posicoes_ocupadas.remove(monstro['posicao'])
            estado['mensagem'] = "Você matou o monstro"

            if monstro['tipo'] == MONSTRO1: # cada tipo de monstro possui uma quantidade diferente de vidas 
                estado['experiencia'] += 2 # experiencia é ganha em caso de morte de monstro - qtd. de experiencia depende do tipo de monstro vencido
            elif monstro['tipo'] == MONSTRO2:
                estado['experiencia'] += 3
            elif monstro['tipo'] == MONSTRO3:
                estado['experiencia'] += 5

        else:
            estado['mensagem'] = f"Você atacou o monstro e agora ele tem {monstro['vida']} vidas"

def coleta_iten_mapa(estado, iten, posicao_itens, posicoes_ocupadas, itens): # definição das especificidades da coleta de itens pelo mapa
    soma_itens = sum(estado['inventario'].values()) # no mapa regular, a quantidade máxima de itens no inventário é restrita a 6

    if soma_itens < 6:
        tipo_iten = iten['tipo'] 
        if tipo_iten == CHAVE and estado['inventario'][tipo_iten] + 1 == 3:
            estado['inventario'][tipo_iten] += 1
            estado['mensagem'] = 'Você desbloqueou a sala secreta' # quando três chaves são coletadas a sala secreta pode ser acessada e a mensagem de aviso é mostrada 
            itens.remove(iten) 
            posicao_itens.remove(iten['posicao'])
            posicoes_ocupadas.remove(iten['posicao'])

        else:
            estado['inventario'][tipo_iten] += 1
            estado['mensagem'] = 'Iten adicionado ao inventário' # enquanto o inventário possuir espaço, ao passar pela posição dos itens eles serão adicionados ao inventário, sendo removidos do mapa
            itens.remove(iten) 
            posicao_itens.remove(iten['posicao'])
            posicoes_ocupadas.remove(iten['posicao']) # as listas de posições ocupadas e posição dos itens são atualizadas de acordo

    else:
        estado['mensagem'] = 'Seu inventário está cheio' # se o inventário não tiver mais espaço, os itens seguirão no mapa para psoterior coleta

def passa_por_objetos(estado): # definição das especificidades das funcionalidades de objetos pelo mapa
    for objeto in estado['objetos']:
        if estado['pos_jogador'] == objeto['posicao']:
            if objeto['tipo'] == ESPINHO: # ao passar por espinhos, o jogador perde uma vida
                if estado['vidas'] > 1:
                    estado['vidas'] -= 1             
                    estado['mensagem'] = "Você perdeu uma vida"
                else:
                    estado['vidas'] -= 1
                    estado['tela_atual'] = TELA_GAME_OVER

            elif objeto['tipo'] == CORACAO: # ao passar por corações, não tendo atingido a vida máxima, o jogador ganha vidas e os corações são removidos do mapa
                if estado['vidas'] == estado['max_vidas']:
                        estado['mensagem'] = "Vida cheia" # se não tiver como coletar vidas por já estar com a vida máxia cheia, os corações seguem no mapa para posterior coleta
                else:
                    estado['vidas'] += 1
                    estado['mensagem'] = "Você ganhou uma vida"
                    estado['objetos'].remove(objeto) 

def coleta_iten_sala_secreta(estado, iten, itens, posicao_itens): # definição das especificidades da coleta de itens na sala secreta
    soma_itens = sum(estado['inventario'].values()) # dentro da sala secreta, como condição bonus, a capacidade do inventário é expandida para 8 itens

    if soma_itens < 8: 
        tipo_iten = iten['tipo']

        estado['inventario'][tipo_iten] += 1
        estado['mensagem'] = 'Item adicionado ao inventário'

        posicao_itens.remove(iten['posicao'])
        itens.remove(iten)
    else:
        estado['mensagem'] = 'Seu inventário está cheio'

def coleta_objeto_sala_secreta(estado, objeto, objetos, posicao_objetos): # definição das especificidades do funcionamento dos itens na sala secreta
    if objeto['tipo'] == CORACAO: # na sala secreta, os corações também funcionam de forma diferente. Ao coletar um coração, a quantidade máxima de vidas que é expandida, dando uma mior capacidade de sobrevivência ao jogador 
        if estado['max_vidas'] < 8: # a coleta de corações se restringe a uma qtd máx de vidas expandida até 8, n sendo permitida a coleta de corações posterior a isso
            estado['max_vidas'] += 1
            estado['vidas'] += 1

            posicao_objetos.remove(objeto['posicao'])
            objetos.remove(objeto)

            estado['mensagem'] = 'Quantidade de vidas aumentada'
        else:
            estado['mensagem'] = 'Você já possui o máximo de 8 vidas' # os corações não coletados seguem no mapa para coleta posterior

def niveis(estado): # define a mudança de níveis
    lista_monstros = [MONSTRO1, MONSTRO2, MONSTRO3]
    mapa = estado['mapa']
    altura_mapa = len(mapa)
    largura_mapa = len(mapa[0])

    monstros = estado['monstros']
    objetos = estado['objetos']
    itens = estado['itens']

    posicoes_ocupadas = [estado['pos_jogador']]
    posicoes_ocupadas.extend(estado['paredes'])

    for objeto in objetos:
        posicoes_ocupadas.append(objeto['posicao'])

    for iten in itens:
        posicoes_ocupadas.append(iten['posicao'])

    for monstro in monstros:
        posicoes_ocupadas.append(monstro['posicao'])

    while estado['experiencia'] >= 10: # ao atingir 10 pontos de experiencia o jogador passa de nível
        estado['nivel'] += 1
        estado['experiencia'] -= 10

        for i in range(4): # a cada mudança de nível, monstros novos são readicionados no mapa
            monstro_sorteado = random.choice(lista_monstros) # o tipo de monstro é escolhido de modo aleatório
            novo_monstro = []
            novo_monstro += gera_objetos(1, monstro_sorteado, ROXO, largura_mapa, altura_mapa, posicoes_ocupadas)

            for novo in novo_monstro:
                if monstro_sorteado == MONSTRO1:
                    novo['vida'] = 5
                    novo['max_vidas'] = 5
                    novo['probabilidade de ataque'] = 0.20

                elif monstro_sorteado == MONSTRO2:
                    novo['vida'] = 3
                    novo['max_vidas'] = 3
                    novo['probabilidade de ataque'] = 0.40
                    novo['eixo'] = None

                elif monstro_sorteado == MONSTRO3:
                    novo['vida'] = 2
                    novo['max_vidas'] = 2
                    novo['probabilidade de ataque'] = 0.60 
                    novo['situação'] = None # os monstros são adicionados de acordo com suas próprias especificidades

                if estado['equipamento'] == 'espada': # considerando a condição de martelo ou espada equipados, as especificidades também devem ser modificadas para que o padrão do momento fique bem definido
                    if novo['tipo'] == MONSTRO1:
                        novo['probabilidade de ataque'] = 0.15 

                    elif novo['tipo'] == MONSTRO2:
                        novo['probabilidade de ataque'] = 0.35

                    elif novo['tipo'] == MONSTRO3:
                        novo['probabilidade de ataque'] = 0.50

                elif estado['equipamento'] == 'martelo':
                    novo['max_vidas'] -= 1
                    novo['vida'] = novo['max_vidas']
                    novo['vida_reduzida_martelo'] = True

                monstros.append(novo) 

        # a passagem de nível também implica a adição de novos objetos e itens ao mapa e estes são adicionados aos dicionarios de estado já existentes
        objetos.extend(gera_objetos(3, CORACAO, VERMELHO, largura_mapa, altura_mapa, posicoes_ocupadas))
        itens.extend(gera_objetos(2, POCAO, COR_POCAO, largura_mapa, altura_mapa, posicoes_ocupadas))
        itens.extend(gera_objetos(1, ELIXIR, COR_ELIXIR, largura_mapa, altura_mapa, posicoes_ocupadas))
        itens.extend(gera_objetos(1, CHAVE, COR_CHAVE, largura_mapa, altura_mapa, posicoes_ocupadas))
        itens.extend(gera_objetos(1, ESPADA, COR_ESPADA, largura_mapa, altura_mapa, posicoes_ocupadas))
        itens.extend(gera_objetos(1, MARTELO, COR_MARTELO, largura_mapa, altura_mapa, posicoes_ocupadas))
