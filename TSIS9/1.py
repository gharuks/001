import pygame, sys
from pygame.locals import *
    
windowSurface = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
PINK = (249, 57, 255)
YELLOW = (255, 241, 73)
ORANGE = (252, 155, 64)
PURPLE = (167, 0, 238)
DARK_GREEN = (58, 158, 73)
WHITE = (255, 255, 255)
BROWN = (85, 46, 46)

pygame.init()
## font setup
font = pygame.font.SysFont("Arial", 17)
clear_text = font.render("  Clear", True, BLACK)
save_text = font.render("  SAVE", True, BLACK)
windowSurface.fill(WHITE)
eraser = pygame.image.load("eraser.png")
draw = False
brush_size = 1
brush_color = GREEN
menu_rect = pygame.Rect(0, 0, 500, 100)
screen_rect = pygame.Rect(0, 100, 500, 400)
green_rect = pygame.Rect(350, 20, 20, 20)
red_rect = pygame.Rect(375, 20, 20, 20)
blue_rect = pygame.Rect(400, 20, 20, 20)
pink_rect = pygame.Rect(425, 20, 20, 20)
black_rect = pygame.Rect(450, 45, 20, 20)
yellow_rect = pygame.Rect(375, 45, 20, 20)
orange_rect = pygame.Rect(350, 45, 20, 20)
purple_rect = pygame.Rect(400, 45, 20, 20)
dark_green_rect = pygame.Rect(450, 20, 20, 20)
brown_rect = pygame.Rect(425, 45, 20, 20)


clear_rect = pygame.Rect(5, 50, 90, 25)

eraser_rect = pygame.Rect(125, 20, 40, 40)

thin_brush = pygame.Rect(200, 20, 85, 2)
medium_brush = pygame.Rect(200, 27, 85, 6)
thick_brush = pygame.Rect(200, 38, 85, 10)
supa_brush = pygame.Rect(200, 53, 85, 20)

save_rect = pygame.Rect(5, 20, 90, 25)
save_flag = False
file_number = 1

def drawLine(screen, start, end, width, color):
    x1 = start[0]
    y1 = start[1]
    x2 = end[0]
    y2 = end[1]

    dx = abs(x1 - x2)
    dy = abs(y1 - y2)

    A = y2 - y1
    B = x1 - x2
    C = x2 * y1 - x1 * y2

    if dx > dy:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1

        for x in range(x1, x2):
            y = (-C - A * x) / B
            pygame.draw.circle(screen, color, (x, y), width)
    else:
        if y1 > y2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        for y in range(y1, y2):
            x = (-C - B * y) / A
            pygame.draw.circle(screen, color, (x, y), width)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            prev = pygame.mouse.get_pos()
            draw = True
        if event.type == MOUSEBUTTONUP:
            draw = False
            prev = None
        if event.type == pygame.MOUSEMOTION:
            mouse_pos = pygame.mouse.get_pos()
            if draw == True and mouse_pos[1] > 100:
                drawLine(windowSurface, prev, mouse_pos, brush_size, brush_color)
            prev = mouse_pos
    if draw == True:    
        if green_rect.collidepoint(mouse_pos):
            brush_color = GREEN
        if red_rect.collidepoint(mouse_pos):
            brush_color = RED
        if blue_rect.collidepoint(mouse_pos):
            brush_color = BLUE
        if pink_rect.collidepoint(mouse_pos):
            brush_color = PINK
        if black_rect.collidepoint(mouse_pos):
            brush_color = BLACK
        if yellow_rect.collidepoint(mouse_pos):
            brush_color = YELLOW
        if orange_rect.collidepoint(mouse_pos):
            brush_color = ORANGE
        if purple_rect.collidepoint(mouse_pos):
            brush_color = PURPLE
        if dark_green_rect.collidepoint(mouse_pos):
            brush_color = DARK_GREEN
        if brown_rect.collidepoint(mouse_pos):
            brush_color = BROWN
        if eraser_rect.collidepoint(mouse_pos):
            brush_color = WHITE
        if clear_rect.collidepoint(mouse_pos):
            pygame.draw.rect(windowSurface, WHITE, screen_rect)
            
    pygame.draw.rect(windowSurface, PURPLE, menu_rect)
    pygame.draw.rect(windowSurface, WHITE, clear_rect)
    windowSurface.blit(clear_text, (13, 50))
    
    pygame.draw.rect(windowSurface, WHITE, save_rect)
    windowSurface.blit(save_text, (13, 25))

    if draw == True and save_flag == False:
        if save_rect.collidepoint(mouse_pos):
            print("File has been saved :P")
            save_surface = pygame.Surface((500, 400))
            save_surface.blit(windowSurface, (0, 0), (0, 100, 500, 400))
            try:
                with open("TSIS9" + str(file_number) + ".png"):
                    print("file already exists")
                    file_number = file_number + 1
                    save_flag = True
            except IOError:
                save_flag = True
                
            pygame.image.save(save_surface, "TSIS9" + str(file_number) + ".png")

    if draw == True:
        if thin_brush.collidepoint(mouse_pos):
            brush_size = 1
        if medium_brush.collidepoint(mouse_pos):
            brush_size = 3
        if thick_brush.collidepoint(mouse_pos):
            brush_size = 5
        if supa_brush.collidepoint(mouse_pos):
            brush_size = 10
    
    pygame.draw.rect(windowSurface, GREEN, green_rect)
    if brush_color == GREEN:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, green_rect, border)
    
    pygame.draw.rect(windowSurface, RED, red_rect)
    if brush_color == RED:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, red_rect, border)
    
    pygame.draw.rect(windowSurface, BLUE, blue_rect)
    if brush_color == BLUE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, blue_rect, border)

    pygame.draw.rect(windowSurface, PINK, pink_rect)
    if brush_color == PINK:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, pink_rect, border)

    pygame.draw.rect(windowSurface, BLACK, black_rect)
    if brush_color == BLACK:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, black_rect, border)

    pygame.draw.rect(windowSurface, YELLOW, yellow_rect)
    if brush_color == YELLOW:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, yellow_rect, border)

    pygame.draw.rect(windowSurface, ORANGE, orange_rect)
    if brush_color == ORANGE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, orange_rect, border)
    
    pygame.draw.rect(windowSurface, ORANGE, orange_rect)
    if brush_color == ORANGE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, orange_rect, border)
    
    pygame.draw.rect(windowSurface, DARK_GREEN, dark_green_rect)
    if brush_color == DARK_GREEN:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, dark_green_rect, border)
    
    pygame.draw.rect(windowSurface, PURPLE, purple_rect)
    if brush_color == PURPLE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, purple_rect, border)
    
    pygame.draw.rect(windowSurface, BROWN, brown_rect)
    if brush_color == BROWN:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, BLACK, brown_rect, border)
    
    windowSurface.blit(eraser, eraser_rect)
    if brush_color == WHITE:
        border = 3
    else:
        border = 1
    pygame.draw.rect(windowSurface, WHITE, eraser_rect, border)

    if brush_size == 1:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.line(windowSurface, BLACK, (200, 20), (285, 20), 2)
    pygame.draw.rect(windowSurface, BLACK, thin_brush, brush_border)
    
    if brush_size == 3:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.line(windowSurface, BLACK, (200, 30), (285, 30), 6)
    pygame.draw.rect(windowSurface, BLACK, medium_brush, brush_border)
    
    if brush_size == 5:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.line(windowSurface, BLACK, (200, 43), (285, 43), 10)
    pygame.draw.rect(windowSurface, BLACK, thick_brush, brush_border)
    
    if brush_size == 10:
        brush_border = 3
    else:
        brush_border = 1
    pygame.draw.line(windowSurface, BLACK, (200, 63), (285, 63), 20)
    pygame.draw.rect(windowSurface, BLACK, supa_brush, brush_border)

    pygame.display.update()
    clock.tick(120)
