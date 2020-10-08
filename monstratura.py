import pygame, os, sys, pathlib, shelve, time
from pygame.locals import *

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
img_iniciar = pygame.image.load('images/btn_iniciar.png')
img_continuar = pygame.image.load('images/btn_continuar.png')
img_opcoes = pygame.image.load('images/btn_opcoes.png')
img_skip = pygame.image.load('images/btn_skip.png')
img_return = pygame.image.load('images/btn_return.png')
img_btn_play = pygame.image.load('images/btn_jogar.png')
img_btn_char = pygame.image.load('images/btn_char.png')
img_btn_inv = pygame.image.load('images/btn_bag.png')
img_btn_album = pygame.image.load('images/btn_album.png')
img_btn_save = pygame.image.load('images/btn_save.png')
# img_btn_options = pygame.image.load('btn_options.png')
img_btn_menu = pygame.image.load('images/btn_menu.png')
img_btn_fem = pygame.image.load('images/btn_mulher.png')
img_btn_masc = pygame.image.load('images/btn_homem.png')
img_btn_magem = pygame.image.load('images/mago.png')
img_btn_archm = pygame.image.load('images/arqueiro.png')
img_btn_swordm = pygame.image.load('images/espado.png')
img_btn_magef = pygame.image.load('images/maga.png')
img_btn_archf = pygame.image.load('images/arqueira.png')
img_btn_swordf = pygame.image.load('images/espada.png')

# create egdes
edge_top = pygame.Rect(10, 10, 1000, 10)
edge_right = pygame.Rect(1000,10,10,600)
edge_bottom = pygame.Rect(10, 600, 1000, 10)
edge_left = pygame.Rect(10, 10, 10, 600)

class player:
    name = None
    sex = None
    profession = None
    level = None
    hit_points = None       
    mana_points = None
    gold = None
    helm = None
    armor = None
    legs = None
    boots = None
    weapon = None
    shield = None
    inventory = {}

player = player()
player.name = 'Matsubi'
player.sex = 'f'
player.profession = 'Arqueira'
player.level = 1

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
        btn = pygame.Rect(410, 230, 200, 50)
        return btn
    if btn_obj == 'c':
        btn = pygame.Rect(410, 310, 200, 50)
        return btn
    if btn_obj == 'o':
        btn = pygame.Rect(410, 390, 200, 50)
        return btn
    if btn_obj == 's':
        btn = pygame.Rect(780, 380, 200,200)
        return btn
    if btn_obj == 'r':
        btn = pygame.Rect(30, 480, 100,100)
        return btn
 
def create_main_buttons(btn_obj):
    if btn_obj == 'p':
        btn = pygame.Rect(775, 440, 50, 50)
        return btn
    if btn_obj == 'c':
        btn = pygame.Rect(845, 440, 50, 50)
        return btn
    if btn_obj == 'i':
        btn = pygame.Rect(920, 440, 50, 50)
        return btn
    if btn_obj == 'a':
        btn = pygame.Rect(775, 520, 50,50)
        return btn
    if btn_obj == 's':
        btn = pygame.Rect(845, 520, 50,50)
        return btn
    if btn_obj == 'm':
        btn = pygame.Rect(920, 520, 50,50)
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
        monstratura_rect = pygame.Rect(95, 42, 837, 77)
        pygame.draw.rect(screen, screen_color, monstratura_rect)
        img_monstratura = pygame.image.load('images/img_monstratura.png')
        mx, my = pygame.mouse.get_pos()
        
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
                new_game()
        if btn_continuar.collidepoint((mx, my)):
            if click:
                if player.name != None:
                    continue_()
        if btn_opcoes.collidepoint((mx, my)):
            if click:
                options()
        
        pygame.draw.rect(screen, (0, 0, 0), btn_iniciar)
        if player.name != None:
            pygame.draw.rect(screen, (0, 0, 0), btn_continuar)
            screen.blit(img_continuar, btn_continuar)

        pygame.draw.rect(screen, (194, 120, 194), edge_top)
        pygame.draw.rect(screen, (194, 120, 194), edge_right)
        pygame.draw.rect(screen, (194, 120, 194), edge_bottom)
        pygame.draw.rect(screen, (194, 120, 194), edge_left)

        screen.blit(img_monstratura, monstratura_rect)
        screen.blit(img_iniciar, btn_iniciar)
        screen.blit(img_opcoes, btn_opcoes)
        pygame.display.update()
        main_clock.tick(60)
        
def new_game():
    hello = 'Olá,'
    welcome = 'bem-vindo ao mundo de Monstratura!'
    begin = 'sua jornada está para começar,'
    cmds = 'mas antes vejamos os comandos básicos...'
    
    running = True
    while running:
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

        screen.blit(img_skip, btn_skip)
        pygame.display.update()
        main_clock.tick(60)
 
def continue_():
    running = True
    while running:
        screen.fill(screen_color)
        mx, my = pygame.mouse.get_pos()
        click = False

        if player.name != None:
            player_frame = pygame.Rect(70, 40, 880, 220)
            pygame.draw.rect(screen, (0,0,0), player_frame, 2)
            player_img = pygame.Rect(100,60,134,184)
            draw_text('Nome:       ' + player.name, consolas, (0, 0, 0), screen, 290, 80)
            draw_text('Profissão:  ' + player.profession, consolas, (0, 0, 0), screen, 290, 120)
            draw_text('Nível:      ' + str(player.level), consolas, (0, 0, 0), screen, 290, 160)
            if player.sex == 'f':
                if player.profession == 'Maga':
                    screen.blit(img_btn_magef, player_img)
                if player.profession == 'Arqueira':
                    screen.blit(img_btn_archf, player_img)
                if player.profession == 'Espadachim':
                    screen.blit(img_btn_swordf, player_img)
            else:
                if player.profession == 'Mago':
                    screen.blit(img_btn_magem, player_img)
                if player.profession == 'Arqueiro':
                    screen.blit(img_btn_archm, player_img)
                if player.profession == 'Espadachim':
                    screen.blit(img_btn_swordm, player_img)
        else:
            draw_text('Nenhum personagem foi criado :(', consolas, (0, 0, 0), screen, 310, 290)
        
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
        
        btn_return = create_initial_buttons('r')
        if btn_return.collidepoint((mx, my)):
            if click:
                initial_menu()
        if player_frame.collidepoint((mx, my)):
            if click:
                game_on()

        pygame.draw.rect(screen, (194, 120, 194), edge_top)
        pygame.draw.rect(screen, (194, 120, 194), edge_right)
        pygame.draw.rect(screen, (194, 120, 194), edge_bottom)
        pygame.draw.rect(screen, (194, 120, 194), edge_left)
        
        screen.blit(img_return, btn_return)
        pygame.display.update()
        main_clock.tick(60)

def options():
    running = True
    while running:
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
        
        options_title = pygame.Rect(455, 30, 95, 33)
        img_title = pygame.image.load('images/title_opcoes.png')
        hotkeys_rect = pygame.Rect(340,100,51,393)
        img_hotkeys = pygame.image.load('images/img_hotkeys.png')
        btn_return = create_initial_buttons('r')
        btn_skip = create_initial_buttons('s')

        if btn_return.collidepoint((mx, my)):
            if click:
                initial_menu()
        if btn_skip.collidepoint((mx, my)):
            if click:
                game_info()
        
        draw_text('Inicia uma rodada', consolas, (0, 0, 0), screen, 410, 115)
        draw_text('Acessa o personagem', consolas, (0, 0, 0), screen, 410, 175)
        draw_text('Acessa o inventário', consolas, (0, 0, 0), screen, 410, 235)
        draw_text('Abre o álbum de cartas', consolas, (0, 0, 0), screen, 410, 295)
        draw_text('Salva o jogo', consolas, (0, 0, 0), screen, 410, 355)
        draw_text('Acessa o menu inicial', consolas, (0, 0, 0), screen, 410, 415)
        draw_text('Retorna à tela anterior', consolas, (0, 0, 0), screen, 410, 470)

        pygame.draw.rect(screen, (194, 120, 194), edge_top)
        pygame.draw.rect(screen, (194, 120, 194), edge_right)
        pygame.draw.rect(screen, (194, 120, 194), edge_bottom)
        pygame.draw.rect(screen, (194, 120, 194), edge_left)

        screen.blit(img_title, options_title)
        screen.blit(img_hotkeys, hotkeys_rect)
        screen.blit(img_return, btn_return)
        screen.blit(img_skip, btn_skip)
        pygame.display.update()
        main_clock.tick(60)

def tutorial():
    running = True
    while running:
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
        
        hotkeys_rect = pygame.Rect(340,100,51,393)
        img_hotkeys = pygame.image.load('images/img_hotkeys.png')
        btn_return = create_initial_buttons('r')
        btn_skip = create_initial_buttons('s')

        if btn_return.collidepoint((mx, my)):
            if click:
                new_game()
        if btn_skip.collidepoint((mx, my)):
            if click:
                char_sex_def()
        
        draw_text('Inicia uma rodada', consolas, (0, 0, 0), screen, 410, 115)
        draw_text('Acessa o personagem', consolas, (0, 0, 0), screen, 410, 175)
        draw_text('Acessa o inventário', consolas, (0, 0, 0), screen, 410, 235)
        draw_text('Abre o álbum de cartas', consolas, (0, 0, 0), screen, 410, 295)
        draw_text('Salva o jogo', consolas, (0, 0, 0), screen, 410, 355)
        draw_text('Acessa o menu inicial', consolas, (0, 0, 0), screen, 410, 415)
        draw_text('Retorna à tela anterior', consolas, (0, 0, 0), screen, 410, 470)

        pygame.draw.rect(screen, (194, 120, 194), edge_top)
        pygame.draw.rect(screen, (194, 120, 194), edge_right)
        pygame.draw.rect(screen, (194, 120, 194), edge_bottom)
        pygame.draw.rect(screen, (194, 120, 194), edge_left)

        screen.blit(img_hotkeys, hotkeys_rect)
        screen.blit(img_return, btn_return)
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
        
        btn_return = create_initial_buttons('r')
        btn_fem = create_char_def_btns('f')
        btn_masc = create_char_def_btns('m')
        
        if btn_fem.collidepoint((mx,my)):
            if click:
                player.sex = 'f'
                char_prfs_fem()
        if btn_masc.collidepoint((mx,my)):
            if click:
                player.sex = 'm'
                char_prfs_male()
        if btn_return.collidepoint((mx, my)):
            if click:
                tutorial()

        pygame.draw.rect(screen, (194, 120, 194), edge_top)
        pygame.draw.rect(screen, (194, 120, 194), edge_right)
        pygame.draw.rect(screen, (194, 120, 194), edge_bottom)
        pygame.draw.rect(screen, (194, 120, 194), edge_left)

        screen.blit(img_btn_fem, btn_fem)
        screen.blit(img_btn_masc, btn_masc)
        screen.blit(img_return, btn_return)
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
        btn_return = create_initial_buttons('r')

        if btn_mage.collidepoint((mx, my)):
            if click:
                player.profession = 'Mago'
                char_name_def()
        if btn_archer.collidepoint((mx, my)):
            if click:
                player.profession = 'Arqueiro'
                char_name_def()
        if btn_sword.collidepoint((mx, my)):
            if click:
                player.profession = 'Espadachim'
                char_name_def()
        if btn_return.collidepoint((mx, my)):
            if click:
                char_sex_def()

        draw_text('Mago', consolas, (0,0,0), screen, 257, 400)
        draw_text('Arqueiro', consolas, (0,0,0), screen, 455, 400)
        draw_text('Espadachim', consolas, (0,0,0), screen, 675, 400)

        pygame.draw.rect(screen, (194, 120, 194), edge_top)
        pygame.draw.rect(screen, (194, 120, 194), edge_right)
        pygame.draw.rect(screen, (194, 120, 194), edge_bottom)
        pygame.draw.rect(screen, (194, 120, 194), edge_left)

        screen.blit(img_btn_magem, btn_mage)
        screen.blit(img_btn_archm, btn_archer)
        screen.blit(img_btn_swordm, btn_sword)
        screen.blit(img_return, btn_return)
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
        btn_return = create_initial_buttons('r')

        if btn_mage.collidepoint((mx, my)):
            if click:
                player.profession = 'Maga'
                char_name_def()
        if btn_archer.collidepoint((mx, my)):
            if click:
                player.profession = 'Arqueira'
                char_name_def()
        if btn_sword.collidepoint((mx, my)):
            if click:
                player.profession = 'Espadachim'
                char_name_def()
        if btn_return.collidepoint((mx, my)):
            if click:
                char_sex_def()

        draw_text('Maga', consolas, (0,0,0), screen, 257, 400)
        draw_text('Arqueira', consolas, (0,0,0), screen, 455, 400)
        draw_text('Espadachim', consolas, (0,0,0), screen, 675, 400)

        pygame.draw.rect(screen, (194, 120, 194), edge_top)
        pygame.draw.rect(screen, (194, 120, 194), edge_right)
        pygame.draw.rect(screen, (194, 120, 194), edge_bottom)
        pygame.draw.rect(screen, (194, 120, 194), edge_left)

        screen.blit(img_btn_magef, btn_mage)
        screen.blit(img_btn_archf, btn_archer)
        screen.blit(img_btn_swordf, btn_sword)
        screen.blit(img_return, btn_return)
        pygame.display.update()
        main_clock.tick(60)

def char_name_def():
    input_rect = pygame.Rect(410,220,200,40)
    user_text = ''
    running = True
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
                if event.key == K_BACKSPACE or event.key == K_ESCAPE:
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
                player.name = user_text
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
        
        img_shelve = pygame.image.load('images/shelve.png')
        shelve_rect = pygame.Rect(120, 100, 552, 411)
        btn_play = create_main_buttons('p')
        btn_char = create_main_buttons('c')
        btn_inv = create_main_buttons('i')
        btn_album = create_main_buttons('a')
        btn_save = create_main_buttons('s')
        btn_menu = create_main_buttons('m')
        
        if btn_inv.collidepoint((mx, my)):
            if click:
                inventory()
        if btn_menu.collidepoint((mx, my)):
            if click:
                initial_menu()
                
        
        pygame.draw.rect(screen, (194, 120, 194), edge_top)
        pygame.draw.rect(screen, (194, 120, 194), edge_right)
        pygame.draw.rect(screen, (194, 120, 194), edge_bottom)
        pygame.draw.rect(screen, (194, 120, 194), edge_left)

        screen.blit(img_shelve, shelve_rect)
        screen.blit(img_btn_play, btn_play)
        screen.blit(img_btn_char, btn_char)
        screen.blit(img_btn_inv, btn_inv)
        screen.blit(img_btn_album, btn_album)
        screen.blit(img_btn_save, btn_save)
        screen.blit(img_btn_menu, btn_menu)
        
        pygame.display.update()
        main_clock.tick(60)

def game_info():
    running = True
    while running:
        screen.fill(screen_color)
        draw_text('Monstratura v0.1 : Todos os direitos reservados', consolas, (0, 0, 0), screen, 70, 150)
        draw_text('Projeto: Paula Moraes', consolas, (0, 0, 0), screen, 70, 250)
        draw_text('E-mail: paulactmoraes@hotmail.com', consolas, (0, 0, 0), screen, 70, 300)
        draw_text('Instagram: @aluaq_', consolas, (0, 0, 0), screen, 70, 350)
        

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
        
        contact_title = pygame.Rect(455, 35, 95, 33)
        img_title = pygame.image.load('images/title_contato.png')
        btn_return = create_initial_buttons('r')

        if btn_return.collidepoint((mx, my)):
            if click:
                options()
        
        line = pygame.Rect(50,200, 920, 5)
        pygame.draw.rect(screen, (194, 120, 194), edge_top)
        pygame.draw.rect(screen, (194, 120, 194), edge_right)
        pygame.draw.rect(screen, (194, 120, 194), edge_bottom)
        pygame.draw.rect(screen, (194, 120, 194), edge_left)
        pygame.draw.rect(screen, (194, 120, 194), line)

        screen.blit(img_title, contact_title)
        screen.blit(img_return, btn_return)
        pygame.display.update()
        main_clock.tick(60)

def inventory():
    running = True
    while running:
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
            
        
        inventory_rect = pygame.Rect(293, 105, 430, 355)
        btn_exit = pygame.Rect(680, 118, 30, 30)
        img_btn_exit = pygame.image.load('images/btn_exit.png')

        if btn_exit.collidepoint((mx, my)):
            if click:
                running = False

        pygame.draw.rect(screen, (194, 120, 194), edge_top)
        pygame.draw.rect(screen, (194, 120, 194), edge_right)
        pygame.draw.rect(screen, (194, 120, 194), edge_bottom)
        pygame.draw.rect(screen, (194, 120, 194), edge_left)
        
        pygame.draw.rect(screen, (127, 80, 53), inventory_rect)
        screen.blit(img_btn_exit, btn_exit)
        pygame.display.update()
        main_clock.tick(60)


initial_menu()