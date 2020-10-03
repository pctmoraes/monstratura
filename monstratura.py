import pygame, os, sys, pathlib, shelve
from pygame.locals import *
from tkinter import font as tkFont

current_dir = pathlib.Path(__file__).parent
os.chdir(current_dir)

main_clock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('M O N S T R A T U R A')
screen = pygame.display.set_mode((1020, 620),0,32)
screen_color = (255,255,200)
click = False

consolas = pygame.font.SysFont('consolas', 24)

# load
img_iniciar = pygame.image.load('btn_iniciar.png')
img_continuar = pygame.image.load('btn_continuar.png')
img_opcoes = pygame.image.load('btn_opcoes.png')

# create egdes
edge_top = pygame.Rect(10, 10, 1000, 10)
edge_right = pygame.Rect(1000,10,10,600)
edge_bottom = pygame.Rect(10, 600, 1000, 10)
edge_left = pygame.Rect(10, 10, 10, 600)

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def create_buttons(btn_obj):
    if btn_obj == 'i':
        btn = pygame.Rect(410, 200, 200, 50)
        return btn
    if btn_obj == 'c':
        btn = pygame.Rect(410, 280, 200, 50)
        return btn
    if btn_obj == 'o':
        btn = pygame.Rect(410, 360, 200, 50)
        return btn
    else:
        pass
 
def main_menu():
    while True:
        screen.fill(screen_color)
        draw_text('menu principal', consolas, (0, 0, 0), screen, 30, 20)

        mx, my = pygame.mouse.get_pos()
        
        # create_buttons(btn_obj)
        btn_iniciar = create_buttons('i')
        btn_continuar = create_buttons('c')
        btn_opcoes = create_buttons('o')        
        
        if btn_iniciar.collidepoint((mx, my)):
            if click:
                start()
        if btn_continuar.collidepoint((mx, my)):
            if click:
                continue_()
        if btn_opcoes.collidepoint((mx, my)):
            if click:
                options()
        
        pygame.draw.rect(screen, (0, 0, 0), btn_iniciar)
        pygame.draw.rect(screen, (0, 0, 0), btn_continuar)
        pygame.draw.rect(screen, (0, 0, 0), btn_opcoes)
        pygame.draw.rect(screen, (194, 120, 194), edge_top)
        pygame.draw.rect(screen, (194, 120, 194), edge_right)
        pygame.draw.rect(screen, (194, 120, 194), edge_bottom)
        pygame.draw.rect(screen, (194, 120, 194), edge_left)

        

        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        screen.blit(img_iniciar, btn_iniciar)
        screen.blit(img_continuar, btn_continuar)
        screen.blit(img_opcoes, btn_opcoes)
        pygame.display.update()
        main_clock.tick(60)
        
def start():
    running = True
    while running:
        screen.fill(screen_color)
        draw_text('iniciar', consolas, (0, 0, 0), screen, 30, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.draw.rect(screen, (194, 120, 194), edge_top)
        pygame.draw.rect(screen, (194, 120, 194), edge_right)
        pygame.draw.rect(screen, (194, 120, 194), edge_bottom)
        pygame.draw.rect(screen, (194, 120, 194), edge_left)
        pygame.display.update()
        main_clock.tick(60)
 
def continue_():
    running = True
    while running:
        screen.fill(screen_color)
 
        draw_text('continuar', consolas, (0, 0, 0), screen, 30, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.draw.rect(screen, (194, 120, 194), edge_top)
        pygame.draw.rect(screen, (194, 120, 194), edge_right)
        pygame.draw.rect(screen, (194, 120, 194), edge_bottom)
        pygame.draw.rect(screen, (194, 120, 194), edge_left)
        pygame.display.update()
        main_clock.tick(60)

def options():
    running = True
    while running:
        screen.fill(screen_color)
        
        draw_text(' opcoes', consolas, (0, 0, 0), screen, 20, 20)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
        
        pygame.draw.rect(screen, (194, 120, 194), edge_top)
        pygame.draw.rect(screen, (194, 120, 194), edge_right)
        pygame.draw.rect(screen, (194, 120, 194), edge_bottom)
        pygame.draw.rect(screen, (194, 120, 194), edge_left)
        pygame.display.update()
        main_clock.tick(60)

# essa função SOMENTE será acionada no botão "Salvar" do menu principal
def save_game(): # passado como parâmetro o objeto Player
    save = shelve.open('save')
    # será atribuida às chaves do save.bak os atributos do player
    # exemplo:
    # save['char_name'] = char.char_name
    # etc
    save.close()

main_menu()