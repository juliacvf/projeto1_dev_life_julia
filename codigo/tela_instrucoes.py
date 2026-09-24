from constantes import *
import motor_grafico as motor


def desenha_tela(janela, estado, altura, largura):
    motor.preenche_fundo(janela, AZUL_CLARO)
    motor.desenha_string(janela, (largura-(len('instrucoes')))//2, 3, 'INSTRUÇÕES', AZUL_CLARO, AMARELO_DOURADO)

    motor.desenha_string(janela, 5, 6, 'COMANDOS:', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 7, 'Aperte a tecla i para acessar seu inventário e retornar à tela do jogo', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 8, 'Dentro da sala secreta, aperte espaço para retornar à tela do jogo', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 9, 'Aperte esc ou a tecla q para sair do jogo', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 10, 'Use as setas para movimentar o personagem', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 11, 'Aperte ↓ para voltar ao menu inicial', AZUL_CLARO, BRANCO)

    motor.desenha_string(janela, 5, 13, 'MONSTROS:', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 14, 'Batalhe com os monstros para ganhar experiência e subir de nível', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 15, 'Monstros do tipo ☠  possuem poder de ataque de 0.70 e 2 vidas', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 16, 'Monstros do tipo ♣ possuem poder de ataque de 0.30 e 5 vidas', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 17, 'Monstros do tipo Ψ possuem poder de ataque de 0.45 e 3 vidas', AZUL_CLARO, BRANCO)
    
    motor.desenha_string(janela, 5, 19, 'ITENS:', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 20, f'Com a espada equipada, você fica mais forte contra os monstros: aperte {'s'}', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 21, f'Com o martelo equipado, monstros têm sua vida reduzida: aperte {'h'}', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 22, f'Poções podem adicionar ou tirar vidas do seu total: aperte {'p'}', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 23, f'O elixir te fornece pontos de experiência: aperte {'e'}', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 24, f'Colete 3 chaves e libere a sala secreta: aperte {'k'}', AZUL_CLARO, BRANCO)
    

    motor.desenha_string(janela, (largura-(len('divirta-se!')))//2, altura-4, 'DIVIRTA-SE!', AZUL_CLARO, BRANCO)
    
    for y in range(2, altura - 2):
            motor.desenha_string(janela, 1, y, '|', AZUL_CLARO, MARROM)
            motor.desenha_string(janela, largura - 2, y, '|', AZUL_CLARO, MARROM)
    
    for x in range(2, largura - 2):
        motor.desenha_string(janela, x, 1, '-', AZUL_CLARO, MARROM)
        motor.desenha_string(janela, x, altura - 2, '-', AZUL_CLARO, MARROM)
    
    motor.desenha_string(janela, 1, 1, '+', AZUL_CLARO, MARROM)
    motor.desenha_string(janela, largura - 2, 1, '+', AZUL_CLARO, MARROM)
    motor.desenha_string(janela, 1, altura - 2, '+', AZUL_CLARO, MARROM)
    motor.desenha_string(janela, largura - 2, altura - 2, '+', AZUL_CLARO, MARROM)
   

                        
    motor.mostra_janela(janela)

def atualiza_estado(estado, tecla):
    if tecla == motor.SETA_BAIXO:
        estado['tela_atual'] = TELA_INICIAL
    elif tecla == motor.ESCAPE or tecla =='q':
        estado['tela_atual'] = SAIR
