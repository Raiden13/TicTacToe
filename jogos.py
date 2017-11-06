

class Jogo(object):
    """
    Um jogo e similar a um problema, mas este contem um valor de utilidade
    para cada estado e um teste de termino em vez de um custo de caminho e
    um teste de objetivo. Um jogo deve herdar esta classe e implementar os
    seus metodos (resultado, utilidade e teste de termino)
    """

    def acoes(self, estado):
        """
        Retorna uma lista de acoes permitidas no estado atual
        """
        raise NotImplementedError

    def result(self, acao, estado):
        """
        Retorna o estado resultante de uma acao aplicada a um estado
        """
        raise NotImplementedError

    def utilidade(self, estado, jogador):
        """
        Retorna o valor de utilidade para o estado atual
        """
        raise NotImplementedError

    def teste_termino(self, estado):
        """
        Retorna True se o estado for um estado final do jogo
        """
        raise NotImplementedError

    def jogador(self, estado):
        """
        Retorna o jogador que realizou o movimento neste estado
        """
        # raise NotImplementedError
        return estado.jogador


def max_value(jogo, estado):
    # Se o estado for um estado terminal
    if jogo.teste_termino(estado):
        # Entao retorne o seu valor de utilidade
        return jogo.utilidade(estado)

    v = float("-inf")

    for acao in jogo.acoes(estado):
        v = max(v, min_value(jogo, jogo.resultado(acao, estado)))

    return v


def min_value(jogo, estado):
    # Se o estado for um estado terminal
    if jogo.teste_termino(estado):
        # entao retorne o seu valor de utilidade
        return jogo.utilidade(estado)

    v = float("inf")

    for acao in jogo.acoes(estado):
        v = min(v, max_value(jogo, jogo.resultado(acao, estado)))

    return v


def minimax(jogo, estado):
    """
    Dado um estado em um jogo, calcular o melhor movimento atraves
    da busca ate os estados finais
    """
    jogador = jogo.jogador(estado)
    resultados = [(a, min_value(jogo.resultado(a, estado))) for a
        in jogo.acoes(estado)]

    return max(resultados, key=lambda r: r[1])
