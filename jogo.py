

class Jogo(object): # Implementando uma "interface" em Python
    """
    A definicao do jogo e similiar a do problema, mas o jogo contem uma
    utilidade para cada estado e um teste de termino em vez de um custo
    de caminho e um objetivo. Para criar um jogo, herde esta classe e
    implemente os metodos "acoes", "resultado", "utilidade" e o "teste_
    termino".
    """

    def acoes(self, estado):
        """
        Retorna uma lista de acoes permitidas para o estado atual.
        @param estado: estado atual do ambiente
        @return: acoes possiveis para este estado
        """
        raise NotImplementedError

    def resultado(self, acao, estado):
        """
        Retorna o estado resultante de uma acao aplicada ao estado
        atual.
        @param acao: uma acao
        @param estado: estado atual do ambiente
        """
        raise NotImplementedError

    def utilidade(self, estado, jogador):
        """
        Retorna o valor de utilidade do estado atual para um determinado
        jogador.
        @param estado: estado atual do ambiente
        @param jogador: jogador que executou o movimento
        @return: o valor de utilidade para o estado atual
        """
        raise NotImplementedError

    def teste_termino(self, estado):
        """
        Retorna True se este for um estado terminal no jogo
        """
        return not self.acoes(estado)

    def jogador(self, estado):
        """
        Retorna o jogador que executou um movimento no estado atual
        """
        return estado.jogador


def minimax(estado, jogo):
    """
    Dado um estado em um jogo, calcula o melhor movimento atraves da busca
    percorrendo todo o caminho ate os estados objetivos.
    @param estado: estado atual do ambiente
    @param jogo: jogo atual
    @return: uma acao
    """
    jogador = jogo.jogador(estado)

    # Funcao que maximiza os ganhos de MAX
    def max_value(estado):
        # Se o estado for um estado terminal, entao
        if jogo.teste_termino(estado):
            # retorne o valor de utilidade para o estado
            return jogo.utilidade(estado, jogador)

        v = float("-inf")

        for a in jogo.acoes(estado):
            v = max(v, min_value(jogo.resultado(a, estado)))

        return v

    # Funcao que minimiza os ganhos de MAX
    def min_value(estado):
        # se o estado for um estado terminal, entao
        if jogo.teste_termino(estado):
            # retorne o valor de utilidade para o estado
            return jogo.utilidade(estado, jogador)

        v = float("inf")

        for a in jogo.acoes(estado):
            v = min(v, max_value(jogo.resultado(a, estado)))

        return v

    # Corpo da funcao minimax
    return max([(a, min_value(jogo.resultado(a, estado)))
                for a in jogo.acoes(estado)], key=lambda r: r[1])[0]
