import pygame
from pygame.locals import *

pygame.init()

screen_width = 450
screen_height = 450

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tic Tac Toe')

line_width = 3
markers = []
clicked = False
pos = []
player = 1

green = (0,255 , 0)
red = (255, 0 , 0)

winner =0
gameover = False
font= pygame.font.SysFont(None, 60)

def draw_grid():
    bg = (192,192, 192)
    grid = (50,50,50)
    screen.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, x * 150), (screen_width, x * 150), line_width)
        pygame.draw.line(screen, grid, (x * 150, 0), (x * 150, screen_height),line_width)

for x in range(3):
    row = [0] *3
    markers.append(row)

print(markers)

def drow_marker():
    x_pos = 0
    for x in  markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, green, (x_pos*150 + 50, y_pos*150 +50),(x_pos*150 + 100, y_pos*150+100),line_width)
                pygame.draw.line(screen, green, (x_pos * 150 + 50, y_pos * 150 + 100),(x_pos * 150 + 100, y_pos * 150 + 50), line_width)
            if y ==-1:
                pygame.draw.circle(screen, red, (x_pos*150 +70,y_pos*150+ 70),40,line_width)
            y_pos+=1
        x_pos +=1

def winner():
    global winner
    global gameover
    y_pos = 0

    for x in markers:
        if sum(x) == 3:
            winner = 1
            gameover = True
        if sum(x) == -3:
            winner = 2
            gameover = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner= 1
            gameover = True
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner= 2
            gameover = True
        y_pos += 1
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        gameover = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        gameover = True


def drow_win(winner):
    win_text = 'Player ' +str(winner) + " Wins!"
    win_show = font.render(win_text, True, (255, 255, 255))
    pygame.draw.rect(screen, green, (screen_width // 2 - 150, screen_height //2 -60, 300 ,70))
    screen.blit(win_show,(screen_width // 2 - 150, screen_height // 2 -40))

run = True
while run:

    draw_grid()
    drow_marker()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if gameover == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if markers[cell_x // 150][cell_y // 150] == 0:
                    markers[cell_x // 150][cell_y // 150] = player
                    player *= -1
                    winner()

    if gameover == True:
        drow_win(winner)

    pygame.display.update()

pygame.quit()