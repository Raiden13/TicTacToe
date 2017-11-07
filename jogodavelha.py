import jogo


class Estado(object):
    """
    Implementacao de um estado no ambiente do jogo da velha
    """

    def __init__(self, jogador, utilidade, tabuleiro, acoes):
        self.jogador = jogador
        self.utilidade = utilidade
        self.tabuleiro = tabuleiro
        self.acoes = acoes


class JogoDaVelha(jogo.Jogo):
    """
    Implementacao da interface "Jogo"
    """

    def __init__(self, estado_inicial):
        self.estado_inicial = estado_inicial
        self.h=3
        self.v=3
        self.k=3

    def acoes(self, estado):
        """
        Movimentos permitidos sao os quadrados que ainda nao foram marcados
        @param estado: estado atual do ambiente
        @return: movimentos que o jogador pode realizar
        """
        return estado.acoes

    def resultado(self, acao, estado):
        """
        Aplica uma acao a um estado e retorna o estado resultante
        @param acao: uma acao
        @param estado: estado atual do ambiente
        @return: novo estado
        """
        # um movimento nao permitido nao surte nenhum efeito
        if acao not in estado.acoes:

            return estado

        tabuleiro = estado.tabuleiro.copy()
        tabuleiro[acao] = estado.jogador
        acoes = estado.acoes.copy()
        acoes.remove(acao)

        return Estado(jogador='O' if estado.jogador=='X' else 'X',
                      utilidade=self.calcula_utilidade(tabuleiro, acao, estado.jogador),
                      tabuleiro=tabuleiro,
                      acoes=acoes)

    def utilidade(self, estado, jogador):
        """
        Retorna o valor de utilidade para o jogador. 1 para vitoria, -1 para derrota e
        0 caso contrario.
        @param estado: estado atual do ambiente
        @param jogador: um dos jogadores
        @return: retorna o valor de utilidade do estado para o jogador
        """
        return estado.utilidade if jogador=='X' else -estado.utilidade

    def teste_termino(self, estado):
        """
        Um estado final e aquele onde ha um vencedor ou onde nao ha quadrados vazios
        """
        return estado.utilidade != 0 or len(estado.acoes) == 0

    def calcula_utilidade(self, board, move, player):
        """
        If 'X' wins with this move, return 1; if 'O' wins return -1; else return 0.
        """
        if (self.k_in_row(board, move, player, (0, 1)) or
                self.k_in_row(board, move, player, (1, 0)) or
                self.k_in_row(board, move, player, (1, -1)) or
                self.k_in_row(board, move, player, (1, 1))):
            return +1 if player == 'X' else -1
        else:
            return 0

    def k_in_row(self, board, move, player, delta_x_y):
        """
        Return true if there is a line through move on board for player.
        """
        (delta_x, delta_y) = delta_x_y
        x, y = move
        n = 0  # n is number of moves in row
        while board.get((x, y)) == player:
            n += 1
            x, y = x + delta_x, y + delta_y
        x, y = move
        while board.get((x, y)) == player:
            n += 1
            x, y = x - delta_x, y - delta_y
        n -= 1  # Because we counted move itself twice
        return n >= self.k

    def display(self, tabuleiro):
        """
        Exibe o estado na tela
        """
        linha = ""
        
        for i in range(3):
            for j in range(3):
                peca = tabuleiro.get((i, j))

                if not peca is None:
                    linha += peca
                else:
                    linha += "-"

            print(linha)
            linha = ""
