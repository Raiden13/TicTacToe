import jogos


class Estado(object):

	def __init__(self, jogador, utilidade, tabuleiro, acoes):
		self.jogador = jogador
		self.utilidade = utilidade
		self.tabuleiro = tabuleiro
		self.acoes = acoes


class JogoDaVelha(jogos.Jogo):

	def acoes(self, estado):
		"""
		Acoes validas sao quaisquer quadrados ainda nao marcados
		"""
		return estado.acoes

	def resultado(self, acao, estado):
		"""
        Retorna o estado resultante de uma acao aplicada a um estado
        """
		# Uma acao invalida nao surte nenhum efeito
		if acao not in estado.acoes:

			return estado

		tabuleiro = estado.tabuleiro.copy()
		tabuleiro[acao] = estado.jogador
		acoes = estado.acoes.copy()
		acoes.remove(acao)

		return Estado(jogador='O' if estado.jogador == 'X' else 'X',
			utilidade=calcula_utilidade(tabuleiro, acao, estado.jogador),
			tabuleiro=tabuleiro,
			acoes=acoes)

	def utilidade(self, estado, jogador):
		"""
		Retorna o valor utilidade para o jogador; 1 se MAX vencer, -1
		se MIN ganhar e 0 caso contrario
		"""
		return estado.utilidade if estado.jogador == 'X' else -estado.utilidade

	def teste_termino(self, estado):
		"""
		Um estado terminal eh aquele onde algum jogador ganhou ou se
		nao ha mais nenhum quadrado a ser preenchido
		"""
		return estado.utilidade != 0 or len(estado.acoes) == 0


def calcula_utilidade(tabuleiro, acao, jogador):
