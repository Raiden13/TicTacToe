import jogodavelha


estado_inicial = jogodavelha.Estado(jogador='X',
	utilidade=0,
	tabuleiro={},
	acoes=[(a, b) for a in range(3) for b in range(3)])
jogo = jogodavelha.JogoDaVelha()

print(estado_inicial)
print(jogo.resultado((0, 0), estado_inicial))
