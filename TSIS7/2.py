import pygame
import math
pygame.init()
SCREEN_WIDHT, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDHT, SCREEN_HEIGHT))
pygame.display.set_caption('My First Game')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: running = False
  screen.fill(WHITE)
  pygame.draw.rect(screen, BLACK, (90, 86, 620, 428), 2)
  pygame.draw.line(screen, BLACK, (90, 300), (710, 300), 2)
  pygame.draw.line(screen, BLACK, (400, 86), (400, 514), 2)
  for step in range(108, 514, 48):
    pygame.draw.line(screen, BLACK, (90, step), (710, step), 1)
  for step in range(112, 710, 96):
    if step==496:
      pygame.draw.line(screen, BLACK, (step, 86), (step, 108), 1)
      pygame.draw.line(screen, BLACK, (step, 156), (step, 514), 1)
    else: pygame.draw.line(screen, BLACK, (step, 86), (step, 514), 1)
  font=pygame.font.SysFont("Times New Roman", 18, italic=True)
  t1=font.render('sin(x)', True, BLACK)
  t2=font.render('cos(x)', True, BLACK)
  screen.blit(t1, (476, 111))
  screen.blit(t2, (476, 131))
  pygame.draw.line(screen, RED, (525, 122), (565, 122))
  for step in range(525, 565, 8):
    pygame.draw.line(screen, BLUE, (step, 142), (step+5, 142))

  for step in range(132, 492, 24):
    pygame.draw.line(screen, BLACK, (90, step), (100, step), 1)
  for step in range(120, 492, 12):
    pygame.draw.line(screen, BLACK, (90, step), (95, step), 1)
  
  for step in range(132, 492, 24):
    pygame.draw.line(screen, BLACK, (710, step), (700, step), 1)
  for step in range(120, 492, 12):
    pygame.draw.line(screen, BLACK, (710, step), (705, step), 1)

  for step in range(160, 688, 48):
    pygame.draw.line(screen, BLACK, (step, 86), (step, 101), 1)
  for step in range(136, 688, 24):
    pygame.draw.line(screen, BLACK, (step, 86), (step, 96), 1)
  for step in range(124, 688, 12):
    pygame.draw.line(screen, BLACK, (step, 86), (step, 91), 1)
  
  for step in range(160, 688, 48):
    pygame.draw.line(screen, BLACK, (step, 514), (step, 499), 1)
  for step in range(136, 688, 24):
    pygame.draw.line(screen, BLACK, (step, 514), (step, 504), 1)
  for step in range(124, 688, 12):
    pygame.draw.line(screen, BLACK, (step, 514), (step, 509), 1)
  
  font=pygame.font.SysFont("Times New Roman", 20, italic=True)
  a=0.75
  dis=0
  while a>=-0.75:
      text=font.render(str(a), True, BLACK)
      if a>0: screen.blit(text, (40, 146+dis))
      else: screen.blit(text, (33, 146+dis))
      dis+=96
      a-=0.50
  poi=['1.00', '0.50', '0.00', '-1.00', '-0.50']
  dis=0
  for x in poi:
      text=font.render(x, True, BLACK)
      if len(x)<=4: screen.blit(text, (40, 98+dis))
      else: screen.blit(text, (33, 98+dis))
      dis+=96
  b=-3
  dis=0
  while b<=3:
      if b%1!=0.5:
          if b==-1:
            text=font.render('-π', True, BLACK)
            screen.blit(text, (99+dis, 525))
          elif b==1:
            text=font.render('π', True, BLACK)
            screen.blit(text, (105+dis, 525))
          elif b<0:
            text=font.render(str(int(b))+'π', True, BLACK)
            screen.blit(text, (93+dis, 525))
          elif b>0:
            text=font.render(str(int(b))+'π', True, BLACK)
            screen.blit(text, (100+dis, 525))
      elif b%1==0.5:
          if b==0.5:
            text=font.render("π", True, BLACK)
            screen.blit(text, (105+dis, 515))
            l=font.render('__', True, BLACK)
            screen.blit(l, (100+dis, 515))
            u=font.render('2', True, BLACK)
            screen.blit(u, (105+dis, 535)) 
          elif b==-0.5:
            text=font.render("-π", True, BLACK)
            screen.blit(text, (100+dis, 515))
            l=font.render('__', True, BLACK)
            screen.blit(l, (100+dis, 515))
            u=font.render('2', True, BLACK)
            screen.blit(u, (105+dis, 535))
          elif b<0:
            text=font.render(str(int(b*2))+"π", True, BLACK)
            screen.blit(text, (93+dis, 515))
            l=font.render('__', True, BLACK)
            screen.blit(l, (99+dis, 515))
            u=font.render('2', True, BLACK)
            screen.blit(u, (103+dis, 535))
          elif b>0:
            text=font.render(str(int(b*2))+"π", True, BLACK)
            screen.blit(text, (100+dis, 515))  
            l=font.render('__', True, BLACK)
            screen.blit(l, (100+dis, 515))
            u=font.render('2', True, BLACK)
            screen.blit(u, (103+dis, 535))       
      dis+=48
      b+=0.5
  text=font.render('0', True, BLACK)
  screen.blit(text, (395, 525))
  font=pygame.font.SysFont("Times New Roman", 30, italic=True)
  text=font.render('x', True, BLACK)
  screen.blit(text, (390, 555))
  for dis in range(0,3):
    font=pygame.font.SysFont("Times New Roman", 15, italic=True)
    t=font.render(str(-3+dis), True, BLACK)
    screen.blit(t, (113+dis*80, 327))
  #graphofcos
  # x=-3*math.pi
  # x0=112
  # while(x0<=688):
  #   pygame.draw.aalines(screen, BLUE, False, [(x0, 300-192*math.cos(x)),(x0, 300-192*math.cos(x))])
  #   x0+=1/10.4
  #   x+=math.pi/1000
  for x in range(112,688,3):
    pygame.draw.aalines(screen, BLUE, False, [(x, 300+192*math.cos((x-112)/96*math.pi)),(x+1, 300+192*math.cos((x-111)/96*math.pi))])
 #graphofsin
  # x=-3*math.pi
  # x0=112
  # while x0<=688:
  #     pygame.draw.aalines(screen, RED, False, [(x0, 300-192*math.sin(x)),(x0+1/10.4, 300-192*math.sin(x))])
  #     x0+=1/10.4
  #     x+=math.pi/1000 
  for i in range(112,688):
    pygame.draw.aalines(screen, RED, False, [(i, 300+192*math.sin((i-112)/96*math.pi)),(i+1, 300+192*math.sin((i-111)/96*math.pi))])
  pygame.display.flip()
pygame.quit()