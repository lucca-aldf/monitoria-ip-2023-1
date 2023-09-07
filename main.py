import pygame as pg

class Estudante:
    
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


estudante_1 = Estudante('Pedro', 18)
estudante_2 = Estudante('Marcus', 19)

print(estudante_1.nome)

DISPLAY_LARGURA = 1280
DISPLAY_ALTURA = 640
DISPLAY_RESOLUCAO = (DISPLAY_LARGURA, DISPLAY_ALTURA)


pg.init()

display_tela = pg.display.set_mode(DISPLAY_RESOLUCAO)

relogio = pg.time.Clock()
rodando = True
while rodando:
    for evento in pg.event.get():
        if evento.type == pg.QUIT or (evento.type == pg.KEYDOWN and pg.key.get_pressed()[pg.K_ESCAPE]):
            rodando = False
            break
    
    relogio.tick(60)
    print(relogio.get_fps())

pg.quit()