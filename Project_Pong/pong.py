### IMPORTS
import pygame, time, sys


### COLORS
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

### CONSTANTS
WIDTH = 900
HEIGHT = 600
pygame.font.init()
COMIC = pygame.font.SysFont('Comic Sans MS', 50)
largeText1 = pygame.font.SysFont('Times new roman', 50)
largeText2 = pygame.font.SysFont('Times new roman', 100)
pygame.mixer.pre_init(44100, 16, 2, 4096)
pygame.init()
image = pygame.image.load('abc4.png')
image1 = pygame.image.load('Try.png')
image2 = pygame.image.load('wins.png')
sound1 = pygame.mixer.Sound("fail.wav")
sound2 = pygame.mixer.Sound("border.wav")
sound3 = pygame.mixer.Sound("bat+hit+ball.wav")
sound4 = pygame.mixer.Sound("click.aif")
music = pygame.mixer.music.load("alan.mp3")
pygame.mixer.music.play(-1)

### VARIABLES
wt = 10

score = 3

PAD1_X = 5
PAD1_Y = HEIGHT/2 - HEIGHT/8

PAD2_X = WIDTH-20
PAD2_Y = HEIGHT/2 - HEIGHT/8

PLAYER1_SCORE = 0
PLAYER2_SCORE = 0

w_p =False
s_p = False
wsr = False
d_p = False
u_p = False
udr = False

dm = HEIGHT/40

PAD_WIDTH = WIDTH/60
PAD_HEIGHT = HEIGHT/4

bsd = 1

BALL_X = WIDTH - WIDTH/4
BALL_Y = HEIGHT/2
BALL_WIDTH = WIDTH/70
BALL_X_VELOCITY =  HEIGHT/60
BALL_X_VELOCITY = -BALL_X_VELOCITY
BALL_Y_VELOCITY = 0

### FUNCTIONS
def drawpad(x, y, w, h):
    pygame.draw.rect(TWO_PLAYER, BLUE,  (x, y, w, h))
    
def rectangle(z, x, y, x1, y1):
    pygame.draw.rect(z , BLUE,  (x, y, x1, y1), 1)
    
def rec(z, x, y, x1, y1):
    pygame.draw.rect(z , YELLOW,  (x, y, x1, y1))

def drawball(x, y):
    pygame.draw.circle(TWO_PLAYER, RED, (int(x), int(y)), int(BALL_WIDTH))

def uploc():
    global PAD2_Y
    global PAD1_Y
    if w_p:
        if PAD1_Y - (dm) < 0:
            PAD1_Y = 0
        else:
            PAD1_Y -= dm
    elif s_p:
        if PAD1_Y + (dm) + PAD_HEIGHT > HEIGHT:
            PAD1_Y = HEIGHT - PAD_HEIGHT
        else:
            PAD1_Y += dm
    if u_p:
        if PAD2_Y - (dm) < 0:
            PAD2_Y = 0
        else:
            PAD2_Y -= dm
    elif d_p:
        if PAD2_Y + (dm) + PAD_HEIGHT > HEIGHT:
            PAD2_Y = HEIGHT - PAD_HEIGHT
        else:
            PAD2_Y += dm

def upblnv(): 
    global BALL_X
    global BALL_X_VELOCITY
    global BALL_Y
    global BALL_Y_VELOCITY
    global PLAYER1_SCORE
    global PLAYER2_SCORE

    if (BALL_X + BALL_X_VELOCITY < PAD1_X + PAD_WIDTH) and ((PAD1_Y < BALL_Y + BALL_Y_VELOCITY + BALL_WIDTH) and (BALL_Y + BALL_Y_VELOCITY - BALL_WIDTH < PAD1_Y + PAD_HEIGHT)):
        pygame.mixer.Sound.play(sound3)
        BALL_X_VELOCITY = -(BALL_X_VELOCITY-(1/10))
        BALL_Y_VELOCITY = ((PAD1_Y + (PAD1_Y + PAD_HEIGHT))/2) - BALL_Y
        BALL_Y_VELOCITY = -BALL_Y_VELOCITY/((5*BALL_WIDTH)/7)
    elif BALL_X + BALL_X_VELOCITY < 0:
        pygame.mixer.Sound.play(sound1)
        PLAYER2_SCORE +=1
        BALL_X = WIDTH/4
        BALL_Y = HEIGHT/2
        BALL_X_VELOCITY = HEIGHT/60
        BALL_Y_VELOCITY = 0
    if (BALL_X + BALL_X_VELOCITY > PAD2_X) and ((PAD2_Y < BALL_Y_VELOCITY + BALL_Y + BALL_WIDTH) and (BALL_Y +BALL_Y_VELOCITY - BALL_WIDTH < PAD2_Y + PAD_HEIGHT)):
        pygame.mixer.Sound.play(sound3)
        BALL_X_VELOCITY = - (BALL_X_VELOCITY+(1/10))
        BALL_Y_VELOCITY = ((PAD2_Y + (PAD2_Y + PAD_HEIGHT))/2) - BALL_Y
        BALL_Y_VELOCITY = -BALL_Y_VELOCITY/((5*BALL_WIDTH)/7)
    elif BALL_X + BALL_X_VELOCITY > WIDTH:
        pygame.mixer.Sound.play(sound1)
        PLAYER1_SCORE +=1
        BALL_X = WIDTH - WIDTH/4
        BALL_Y = HEIGHT/2
        BALL_X_VELOCITY = -HEIGHT/60
        BALL_Y_VELOCITY = 0
    if BALL_Y + BALL_Y_VELOCITY > HEIGHT or BALL_Y + BALL_Y_VELOCITY < 0:
        pygame.mixer.Sound.play(sound2)
        BALL_Y_VELOCITY = - BALL_Y_VELOCITY

    BALL_Y += BALL_Y_VELOCITY
    BALL_X += BALL_X_VELOCITY

def drawscore():
    SCORE = largeText1.render(str(PLAYER1_SCORE)+"     "+str(PLAYER2_SCORE), False, WHITE)
    TWO_PLAYER.blit(SCORE, (WIDTH/2-63, 30))

### INITIALIZE
TWO_PLAYER = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
TWO_PLAYER.fill(BLACK)
WINS = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
WINS.fill(BLACK)
MENUPAUSE = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
MENUPAUSE.fill(BLACK)
HELP = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
HELP.fill(BLACK)
TRY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
TRY.fill(BLACK)
MENU = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
MENU.fill(BLACK)
pygame.display.flip()

helpText1 = COMIC.render("1'ST PLAYER:", True, YELLOW)
helpText2 = COMIC.render("KEY 'W' : UP", True, YELLOW)
helpText3 = COMIC.render("KEY 'S' : DOWN", True, YELLOW)
helpText4 = COMIC.render("2'ST PLAYER:", True, RED)
helpText5 = COMIC.render("KEY 'UP' : UP", True, RED)
helpText6 = COMIC.render("KEY 'DOWN' : DOWN", True, RED)
help_ = largeText1.render("HELP", True, YELLOW)
play_ = largeText1.render("PLAY", True, YELLOW)
exit_ = largeText1.render("EXIT", True, YELLOW)
continue_ = largeText1.render("CONTINUE", True, YELLOW)
try_ = largeText1.render("TRY AGAIN", True, YELLOW)
menu_ = largeText1.render("MENU", True, YELLOW)
menu_title = largeText2.render("PING-PONG", True, YELLOW)
p2w = largeText2.render("PLAYER 2 WINS", True, GREEN)
p1w = largeText2.render("PLAYER 1 WINS", True, GREEN)

try_to = False
menu = True
helping = False
helpi = False
menuPause = False
running = False
wins = False

def Menu():
    global running, menu, helping, image, help_, play_, exit_, menu_title
    while menu:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()   
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 20<=mx<=150 and 350<=my<=394:
                    pygame.mixer.Sound.play(sound4)
                    menu = False
                    running = True
                elif 20<=mx<=155 and 400<=my<=444:
                    pygame.mixer.Sound.play(sound4)
                    menu = False
                    helping = True
                elif 20<=mx<=148 and 450<=my<=494:
                    pygame.mixer.Sound.play(sound4)
                    pygame.quit()
                    sys.exit()
        MENU.blit(image, (-2,-1))
        rectangle(MENU, 20, 350, 130, 44)
        rectangle(MENU, 20, 400, 135, 44)
        rectangle(MENU, 20, 450, 128, 44)
        rec(MENU, 150, 180, 600, 4)
        MENU.blit(play_, (23, 345))
        MENU.blit(help_, (23, 395))
        MENU.blit(exit_, (23, 445))
        MENU.blit(menu_title, (180, 80))
        pygame.display.update()

def MenuandPause():
    global running, menu, menuPause, helpi, image, help_, exit_, continue_
    while menuPause:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = True
                    menuPause = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 20<=mx<=300 and 350<=my<=394:
                    pygame.mixer.Sound.play(sound4)
                    menuPause = False
                    running = True
                elif 20<=mx<=155 and 400<=my<=444:
                    pygame.mixer.Sound.play(sound4)
                    menuPause = False
                    helpi = True
                elif 20<=mx<=148 and 450<=my<=494:
                    pygame.mixer.Sound.play(sound4)
                    pygame.quit()
                    sys.exit()
        MENUPAUSE.blit(image, (-2,-1))
        rectangle(MENU, 20, 350, 280, 44)
        rectangle(MENU, 20, 400, 135, 44)
        rectangle(MENU, 20, 450, 128, 44)
        rec(MENU, 150, 180, 600, 4)
        MENUPAUSE.blit(continue_, (23, 345))
        MENUPAUSE.blit(help_, (23, 395))
        MENUPAUSE.blit(exit_, (23, 445))
        MENU.blit(menu_title, (180, 80))
        pygame.display.update()

def Try():
    global try_to, running, menu, image, try_, menu_, exit_ 
    while try_to:
        mx, my = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if 20<=mx<=305 and 250<=my<=294:
                    pygame.mixer.Sound.play(sound4)
                    try_to = False
                    running = True
                elif 20<=mx<=170 and 300<=my<=344:
                    pygame.mixer.Sound.play(sound4)
                    try_to = False
                    menu = True
                elif 20<=mx<=148 and 350<=my<=394:
                    pygame.mixer.Sound.play(sound4)
                    pygame.quit()
                    sys.exit()
        MENU.blit(image1, (-2,-1))
        rectangle(MENU, 20, 250, 285, 44)
        rectangle(MENU, 20, 300, 150, 44)
        rectangle(MENU, 20, 350, 128, 44)
        MENU.blit(try_, (23, 245))
        MENU.blit(menu_, (23, 295))
        MENU.blit(exit_, (23, 345))
        MENU.blit(menu_title, (20, 50))
        pygame.display.update()

def Win():
    global p1w, p2w, wins, try_to, PLAYER2_SCORE, PLAYER1_SCORE
    while wins:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mixer.Sound.play(sound4)
                    wins = False
                    try_to = True
                    PLAYER1_SCORE = 0
                    PLAYER2_SCORE = 0
        WINS.blit(image2, (0,0))
        if PLAYER1_SCORE > PLAYER2_SCORE:
            WINS.blit(p1w, (80, 230))
        else:
            WINS.blit(p2w, (80, 230))
        pygame.display.update()

def Help():
    global menu, helping
    while helping:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mixer.Sound.play(sound4)
                    helping = False
                    menu = True
        HELP.blit(image1, (0, 0))
        HELP.blit(helpText1, (100, 50))
        HELP.blit(helpText2, (300, 100))
        HELP.blit(helpText3, (300, 150))
        HELP.blit(helpText4, (100, 300))
        HELP.blit(helpText5, (300, 350))
        HELP.blit(helpText6, (300,400))
        pygame.display.update()

def Helping():
    global menuPause, helpi
    while helpi:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pygame.mixer.Sound.play(sound4)
                    helpi = False
                    menuPause = True
        HELP.blit(image1, (0, 0))
        HELP.blit(helpText1, (100, 50))
        HELP.blit(helpText2, (300, 100))
        HELP.blit(helpText3, (300, 150))
        HELP.blit(helpText4, (100, 300))
        HELP.blit(helpText5, (300, 350))
        HELP.blit(helpText6, (300, 400))
        pygame.display.update()
                    

def Running():
    global running, try_to, menu, menuPause, wins, w_p, s_p, wsr, u_p, d_p, udr, PAD1_X, PAD1_Y, PAD_WIDTH, PAD_HEIGHT, PAD2_X, BLACK,  PAD2_Y,BALL_X, BALL_Y, wt, PLAYER2_SCORE, PLAYER1_SCORE
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    menuPause = True
                if event.key == pygame.K_w:
                    w_p = True
                    if s_p == True:
                        s_p = False
                        wsr = True
                if event.key == pygame.K_s:
                    s_p = True
                    if w_p == True:
                        w_p = False
                        wsr = True
                if event.key == pygame.K_UP:
                    u_p = True
                    if d_p == True:
                        d_p = False
                        udr = True
                if event.key == pygame.K_DOWN:
                    d_p = True
                    if u_p == True:
                        u_p = False
                        udr = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    w_p = False
                    if wsr == True:
                        s_p = True
                        wsr = False
                if event.key == pygame.K_s:
                    s_p = False
                    if wsr == True:
                        w_p = True
                        wsr = False
                if event.key == pygame.K_UP:
                    u_p = False
                    if udr == True:
                        d_p = True
                        udr = False
                if event.key == pygame.K_DOWN:
                    d_p = False
                    if udr == True:
                        u_p = True
                        udr = False
        if PLAYER1_SCORE >= score:
            TWO_PLAYER.blit(p1w, (300, 300))
            running = False
            wins = True
            PAD1_X = 5
            PAD1_Y = HEIGHT/2 - HEIGHT/8
            PAD2_X = WIDTH-20
            PAD2_Y = HEIGHT/2 - HEIGHT/8
            BALL_X = WIDTH/2
            BALL_Y = HEIGHT/2
        elif PLAYER2_SCORE >= score:
            TWO_PLAYER.blit(p2w, (300, 300))
            running = False
            wins = True
            PAD1_X = 5
            PAD1_Y = HEIGHT/2 - HEIGHT/8
            PAD2_X = WIDTH-20
            PAD2_Y = HEIGHT/2 - HEIGHT/8
            BALL_X = WIDTH/2
            BALL_Y = HEIGHT/2
        TWO_PLAYER.fill(BLACK)
        uploc()
        upblnv()
        drawscore()
        drawball(BALL_X, BALL_Y)
        drawpad(PAD1_X, PAD1_Y, PAD_WIDTH, PAD_HEIGHT)
        drawpad(PAD2_X, PAD2_Y, PAD_WIDTH, PAD_HEIGHT)
        pygame.draw.rect(TWO_PLAYER, BLUE, (0, 0, WIDTH, HEIGHT), 2)
        pygame.draw.rect(TWO_PLAYER, WHITE, (WIDTH/2, 1, 0, HEIGHT-2), 2)
        pygame.display.flip()
        pygame.time.wait(wt)

def RunAll():
    global running, menu, try_to, helpi, helping, wins
    if running == True:
        Running()
        RunAll()
    elif try_to == True:
        Try()
        RunAll()
    elif menu == True:
        Menu()
        RunAll()
    elif menuPause == True:
        MenuandPause()
        RunAll()
    elif wins == True:
        Win()
        RunAll()
    elif helpi == True:
        Helping()
        RunAll()
    elif helping == True:
        Help()
        RunAll()
    else:
        print("BUG")
RunAll()

