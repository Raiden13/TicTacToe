import jogo
import jogodavelha


# Estado inicial do jogo
estado_atual = jogodavelha.Estado(jogador='X',
                                    utilidade=0,
                                    tabuleiro={},
                                    acoes=[(i, j) for i in range(3) for j in range(3)])

jogo_da_velha = jogodavelha.JogoDaVelha(estado_atual)


while not jogo_da_velha.teste_termino(estado_atual):
    acao = jogo.minimax(estado_atual, jogo_da_velha)
    estado_atual = jogo_da_velha.resultado(acao, estado_atual)
    print(":.: ---- :.:")
    jogo_da_velha.display(estado_atual.tabuleiro)
    print(":.: ---- :.:")
