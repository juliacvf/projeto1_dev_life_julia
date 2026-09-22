from constantes import *
import motor_grafico as motor


def desenha_tela(janela, estado, altura, largura):
    motor.preenche_fundo(janela, AZUL_CLARO)
    motor.desenha_string(janela, (largura-(len('instrucoes')))//2, 5, 'INSTRUÇÕES', AZUL_CLARO, AMARELO_DOURADO)
    motor.desenha_string(janela, 5, 9, '1 - Use as setas para movimentar o personagem', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 10, '2 - Batalhe com os monstros para ganhar experiência e subir de nível', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 11, '3 - Monstros do tipo ♣ possuem poder de ataque de 0.2 e 5 vidas', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 12, '4 - Monstros do tipo ♠ possuem poder de ataque de 0.4 e 3 vidas', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 13, '5 - Monstros do tipo X possuem poder de ataque de 0.6 e 2 vidas', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 14, '6 - Colete e armazene itens que podem oferecer vantagens e tome cuidado com as armadilhas', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 15, '7 - Aperte a tecla i para acessar seu inventário', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 16, '8 - Aperte esc ou a tecla q para sair do jogo', AZUL_CLARO, BRANCO)
    motor.desenha_string(janela, 5, 17, '9 - Aperte ↓ para voltar ao menu inicial', AZUL_CLARO, BRANCO)
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
