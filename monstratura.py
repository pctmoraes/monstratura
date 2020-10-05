import pygame, os, sys, pathlib, shelve, time
from pygame.locals import *
# from tkinter import font as tkFont

current_dir = pathlib.Path(__file__).parent
os.chdir(current_dir)

pygame.init()
main_clock = pygame.time.Clock()
pygame.display.set_caption('M O N S T R A T U R A')
screen = pygame.display.set_mode((1020, 620),0,32)
screen_color = (255,255,200)
consolas = pygame.font.SysFont('consolas', 24)
click = False

# image load
img_iniciar = pygame.image.load('btn_iniciar.png')
img_continuar = pygame.image.load('btn_continuar.png')
img_opcoes = pygame.image.load('btn_opcoes.png')
img_skip = pygame.image.load('btn_skip.png')
img_btn_play = pygame.image.load('btn_jogar.png')
img_btn_char = pygame.image.load('btn_char.png')
img_btn_inv = pygame.image.load('btn_bag.png')
img_btn_save = pygame.image.load('btn_save.png')
img_btn_options = pygame.image.load('btn_options.png')
img_btn_menu = pygame.image.load('btn_menu.png')
img_btn_fem = pygame.image.load('btn_mulher.png')
img_btn_masc = pygame.image.load('btn_homem.png')
img_btn_magem = pygame.image.load('mago.png')
img_btn_archm = pygame.image.load('arqueiro.png')
img_btn_swordm = pygame.image.load('espado.png')
img_btn_magef = pygame.image.load('maga.png')
img_btn_archf = pygame.image.load('arqueira.png')
img_btn_swordf = pygame.image.load('espada.png')

# create egdes
edge_top = pygame.Rect(10, 10, 1000, 10)
edge_right = pygame.Rect(1000,10,10,600)
edge_bottom = pygame.Rect(10, 600, 1000, 10)
edge_left = pygame.Rect(10, 10, 10, 600)

def blit_text(surface, text, pos, font, color):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

def create_initial_buttons(btn_obj):
    if btn_obj == 'i':
        btn = pygame.Rect(410, 200, 200, 50)
        return btn
    if btn_obj == 'c':
        btn = pygame.Rect(410, 280, 200, 50)
        return btn
    if btn_obj == 'o':
        btn = pygame.Rect(410, 360, 200, 50)
        return btn
    if btn_obj == 's':
        btn = pygame.Rect(780, 380, 200,200)
        return btn
 
def create_main_buttons(btn_obj):
    if btn_obj == 'p':
        btn = pygame.Rect(80, 100, 50, 50)
        return btn
    if btn_obj == 'c':
        btn = pygame.Rect(80, 160, 50, 50)
        return btn
    if btn_obj == 'i':
        btn = pygame.Rect(80, 220, 50, 50)
        return btn
    if btn_obj == 's':
        btn = pygame.Rect(80, 280, 50,50)
        return btn
    if btn_obj == 'o':
        btn = pygame.Rect(80, 340, 50,50)
        return btn
    if btn_obj == 'm':
        btn = pygame.Rect(80, 400, 50,50)
        return btn

def create_char_def_btns(btn_obj):
    if btn_obj == 'f':
        btn = pygame.Rect(270, 250, 150, 50)
        return btn
    if btn_obj == 'm':
        btn = pygame.Rect(540, 250, 150, 50)
        return btn
    if btn_obj == 'mage':
        btn = pygame.Rect(215, 200, 134, 184)
        return btn
    if btn_obj == 'arch':
        btn = pygame.Rect(435, 200, 134, 184)
        return btn
    if btn_obj == 'sword':
        btn = pygame.Rect(670, 200, 134, 184)
        return btn

def initial_menu():
    while True:
        screen.fill(screen_color)
        draw_text('menu inicial', consolas, (0, 0, 0), screen, 30, 20)

        mx, my = pygame.mouse.get_pos()
        
        # create_initial_buttons(btn_obj)
        btn_iniciar = create_initial_buttons('i')
        btn_continuar = create_initial_buttons('c')
        btn_opcoes = create_initial_buttons('o')        
        
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
    
        screen.blit(img_iniciar, btn_iniciar)
        screen.blit(img_continuar, btn_continuar)
        screen.blit(img_opcoes, btn_opcoes)
        pygame.display.update()
        main_clock.tick(60)
        
def start():
    running = True
    while running:
        hello = 'Olá,'
        welcome = 'bem-vindo ao mundo de Monstratura!'
        begin = 'sua jornada está para começar,'
        cmds = 'mas antes vejamos os comandos básicos...'
        screen.fill(screen_color)
        draw_text(hello, consolas, (0,0,0), screen, 480, 150)
        draw_text(welcome, consolas, (0,0,0), screen, 300, 240)
        draw_text(begin, consolas, (0,0,0), screen, 320, 300)
        draw_text(cmds, consolas, (0, 0, 0), screen, 270, 350)
        mx, my = pygame.mouse.get_pos()
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        btn_skip = create_initial_buttons('s')
        if btn_skip.collidepoint((mx, my)):
            if click:
                tutorial()
        
        pygame.draw.rect(screen, (194, 120, 194), edge_top)
        pygame.draw.rect(screen, (194, 120, 194), edge_right)
        pygame.draw.rect(screen, (194, 120, 194), edge_bottom)
        pygame.draw.rect(screen, (194, 120, 194), edge_left)
        pygame.draw.rect(screen, (0, 0, 0), btn_skip)

        screen.blit(img_skip, btn_skip)
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

def tutorial():
    running = True
    while running:
        current_time = pygame.time.get_ticks()
        screen.fill(screen_color)
        mx, my = pygame.mouse.get_pos()
        click = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        btn_skip = create_initial_buttons('s')
        btn_play = create_main_buttons('p')
        btn_char = create_main_buttons('c')
        btn_inv = create_main_buttons('i')
        btn_save = create_main_buttons('s')
        btn_options = create_main_buttons('o')
        btn_menu = create_main_buttons('m')

        if btn_skip.collidepoint((mx, my)):
            if click:
                char_sex_def()
            
        if not click:
            if not (current_time < 6000): #6000
                draw_text('Ao clicar aqui você inicia uma rodada', consolas, (0, 0, 0), screen, 160, 115)
                pygame.draw.rect(screen, (0, 0, 0), btn_play)
                screen.blit(img_btn_play, btn_play)
            if not (current_time < 8000):#8000
                draw_text('Ao clicar aqui você acessa seu personagem', consolas, (0, 0, 0), screen, 160, 175)
                pygame.draw.rect(screen, (0, 0, 0), btn_char)
                screen.blit(img_btn_char, btn_char)
            if not (current_time < 10000):#10000
                draw_text('Ao clicar aqui você acessa seu inventário', consolas, (0, 0, 0), screen, 160, 235)
                pygame.draw.rect(screen, (0, 0, 0), btn_inv)
                screen.blit(img_btn_inv, btn_inv)
            if not (current_time < 12000):#12000
                draw_text('Ao clicar aqui você salva o jogo', consolas, (0, 0, 0), screen, 160, 295)
                pygame.draw.rect(screen, (0, 0, 0), btn_save)
                screen.blit(img_btn_save, btn_save)
            if not (current_time < 14000):#14000
                draw_text('Ao clicar aqui você acessa as opções', consolas, (0, 0, 0), screen, 160, 355)
                pygame.draw.rect(screen, (0, 0, 0), btn_options)
                screen.blit(img_btn_options, btn_options)
            if not (current_time < 16000):#16000
                draw_text('Ao clicar aqui você acessa o menu inicial', consolas, (0, 0, 0), screen, 160, 415)
                pygame.draw.rect(screen, (0, 0, 0), btn_menu)
                screen.blit(img_btn_menu, btn_menu)
        else:
            char_sex_def()

        pygame.draw.rect(screen, (194, 120, 194), edge_top)
        pygame.draw.rect(screen, (194, 120, 194), edge_right)
        pygame.draw.rect(screen, (194, 120, 194), edge_bottom)
        pygame.draw.rect(screen, (194, 120, 194), edge_left)
        pygame.draw.rect(screen, (0, 0, 0), btn_skip)
        
        screen.blit(img_skip, btn_skip)
        pygame.display.update()
        main_clock.tick(60)

def char_sex_def():
    running = True
    while running:
        screen.fill(screen_color)
        draw_text('Agora iremos criar o personagem.', consolas, (0, 0, 0), screen, 300, 80)
        draw_text('Você é:', consolas, (0, 0, 0), screen, 460, 150)
        mx, my = pygame.mouse.get_pos()
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        btn_fem = create_char_def_btns('f')
        btn_masc = create_char_def_btns('m')
        if btn_fem.collidepoint((mx,my)):
            if click:
                # self.sex = 'f'
                char_prfs_fem()
        if btn_masc.collidepoint((mx,my)):
            if click:
                # self.sex = 'm'
                char_prfs_male()


        pygame.draw.rect(screen, (194, 120, 194), edge_top)
        pygame.draw.rect(screen, (194, 120, 194), edge_right)
        pygame.draw.rect(screen, (194, 120, 194), edge_bottom)
        pygame.draw.rect(screen, (194, 120, 194), edge_left)
        pygame.draw.rect(screen, (0, 0, 0), btn_fem)
        pygame.draw.rect(screen, (0, 0, 0), btn_masc)

        screen.blit(img_btn_fem, btn_fem)
        screen.blit(img_btn_masc, btn_masc)
        pygame.display.update()
        main_clock.tick(60)

def char_prfs_male():
    running = True
    while running:
        screen.fill(screen_color)
        draw_text('Escolha sua profissão', consolas, (0, 0, 0), screen, 360, 80)
        mx, my = pygame.mouse.get_pos()
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        btn_mage = create_char_def_btns('mage')
        btn_archer = create_char_def_btns('arch')
        btn_sword = create_char_def_btns('sword')

        if btn_mage.collidepoint((mx, my)):
            if click:
                options()
        if btn_archer.collidepoint((mx, my)):
            if click:
                options()
        if btn_sword.collidepoint((mx, my)):
            if click:
                options()

        draw_text('Mago', consolas, (0,0,0), screen, 257, 400)
        draw_text('Arqueiro', consolas, (0,0,0), screen, 455, 400)
        draw_text('Espadachim', consolas, (0,0,0), screen, 675, 400)

        pygame.draw.rect(screen, (194, 120, 194), edge_top)
        pygame.draw.rect(screen, (194, 120, 194), edge_right)
        pygame.draw.rect(screen, (194, 120, 194), edge_bottom)
        pygame.draw.rect(screen, (194, 120, 194), edge_left)
        pygame.draw.rect(screen, (255, 255, 255), btn_mage)
        pygame.draw.rect(screen, (255, 255, 255), btn_archer)
        pygame.draw.rect(screen, (255, 255, 255), btn_sword)

        screen.blit(img_btn_magem, btn_mage)
        screen.blit(img_btn_archm, btn_archer)
        screen.blit(img_btn_swordm, btn_sword)
        pygame.display.update()
        main_clock.tick(60)

def char_prfs_fem():
    running = True
    while running:
        screen.fill(screen_color)
        draw_text('Escolha sua profissão', consolas, (0, 0, 0), screen, 360, 80)
        mx, my = pygame.mouse.get_pos()
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        btn_mage = create_char_def_btns('mage')
        btn_archer = create_char_def_btns('arch')
        btn_sword = create_char_def_btns('sword')

        if btn_mage.collidepoint((mx, my)):
            if click:
                # self.profission = mage
                char_name_def()
        if btn_archer.collidepoint((mx, my)):
            if click:
                # self.profission = mage
                char_name_def()
        if btn_sword.collidepoint((mx, my)):
            if click:
                # self.profission = mage
                char_name_def()

        draw_text('Maga', consolas, (0,0,0), screen, 257, 400)
        draw_text('Arqueira', consolas, (0,0,0), screen, 455, 400)
        draw_text('Espadachim', consolas, (0,0,0), screen, 675, 400)

        pygame.draw.rect(screen, (194, 120, 194), edge_top)
        pygame.draw.rect(screen, (194, 120, 194), edge_right)
        pygame.draw.rect(screen, (194, 120, 194), edge_bottom)
        pygame.draw.rect(screen, (194, 120, 194), edge_left)
        pygame.draw.rect(screen, (255, 255, 255), btn_mage)
        pygame.draw.rect(screen, (255, 255, 255), btn_archer)
        pygame.draw.rect(screen, (255, 255, 255), btn_sword)

        screen.blit(img_btn_magef, btn_mage)
        screen.blit(img_btn_archf, btn_archer)
        screen.blit(img_btn_swordf, btn_sword)
        pygame.display.update()
        main_clock.tick(60)

def char_name_def():
    running = True
    input_rect = pygame.Rect(410,220,200,40)
    user_text = ''
    while running:
        screen.fill(screen_color)
        draw_text('Como é o nome do seu personagem?', consolas, (0, 0, 0), screen, 300, 140)
        mx, my = pygame.mouse.get_pos()
        click = False

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.draw.rect(screen, (0,0,0), input_rect, 2)
        text_surface = consolas.render(user_text, True, (0,0,0))
        
        btn_skip = create_initial_buttons('s')
        if btn_skip.collidepoint((mx, my)):
            if click:
        #         self.name = user_text
                game_on()

        pygame.draw.rect(screen, (194, 120, 194), edge_top)
        pygame.draw.rect(screen, (194, 120, 194), edge_right)
        pygame.draw.rect(screen, (194, 120, 194), edge_bottom)
        pygame.draw.rect(screen, (194, 120, 194), edge_left)
        
        screen.blit(text_surface, (input_rect.x + 10, input_rect.y + 10))
        screen.blit(img_skip, btn_skip)
        pygame.display.update()
        main_clock.tick(60)

def game_on():
    running = True
    while running:
        screen.fill(screen_color)
        draw_text(' game on!', consolas, (0, 0, 0), screen, 20, 20)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        
        pygame.draw.rect(screen, (194, 120, 194), edge_top)
        pygame.draw.rect(screen, (194, 120, 194), edge_right)
        pygame.draw.rect(screen, (194, 120, 194), edge_bottom)
        pygame.draw.rect(screen, (194, 120, 194), edge_left)
        pygame.display.update()
        main_clock.tick(60)

initial_menu()