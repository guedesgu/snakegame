#importa biblioteca
import pygame as pg
from random import randrange

WINDOW = 1000
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: (randrange(*RANGE),randrange(*RANGE))
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()
length = 1
segments = [snake.copy()]
snake_dir = (0,0)
time, time_step = 0, 100
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            # movimento para cima
            if event.key == pg.K_w:
                snake_dir = (0, -TILE_SIZE)
            # movimento para baixo
            if event.key == pg.K_s:
                snake_dir = (0, TILE_SIZE)
            # movimento para esquerda    
            if event.key == pg.K_a:
                snake_dir = (-TILE_SIZE, 0)
            # movimento para direita    
            if event.key == pg.K_d:
                snake_dir = (TILE_SIZE, 0)
    # define uma imagem como valor da variavel           
    bgTeste = pg.image.load('image.png')
    # utiliza da imagem que foi definida no valor para aplicar no plano de fundo
    screen.blit(bgTeste, (0, 0))
    # desenha a cobra
    [pg.draw.rect(screen, 'blue', segment) for segment in segments]
    # configurações da movimentação da cobra
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[length:]
    pg.display.flip()
    clock.tick(60)
