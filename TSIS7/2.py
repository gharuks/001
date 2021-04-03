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
    if event.type == pygame.QUIT:
      running = False
  screen.fill(WHITE)
  pygame.draw.rect(screen, BLACK, (90, 86, 620, 428), 2)
  pygame.draw.line(screen, BLACK, (90, 300), (710, 300), 2)
  pygame.draw.line(screen, BLACK, (400, 86), (400, 514), 2)
  for step in range(108, 514, 48):
    pygame.draw.line(screen, BLACK, (90, step), (710, step), 1)
  for step in range(112, 710, 96):
    pygame.draw.line(screen, BLACK, (step, 86), (step, 514), 1)

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
  
  font=pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 20)
  a=0.75
  dis=0
  while a>=0:
      text=font.render(str(a), True, BLACK)
      screen.blit(text, (40, 146+dis))
      dis+=96
      a-=0.50
  a=-0.75
  dis=0
  while a<=0:
      text=font.render(str(a), True, BLACK)
      screen.blit(text, (35, 434+dis))
      dis-=96
      a+=0.50
  text=font.render('0.00', True, BLACK)
  screen.blit(text, (40, 290))
  
  text=font.render('0.50', True, BLACK)
  screen.blit(text, (40, 194))
  
  text=font.render('1.00', True, BLACK)
  screen.blit(text, (40, 98))

  text=font.render('-1.00', True, BLACK)
  screen.blit(text, (35, 482))

  text=font.render('-0.50', True, BLACK)
  screen.blit(text, (35, 386))
  
  b=-3
  dis=0
  while b<=3:
      if b%1!=0.5 and b<0:
          if b==-1:
            text=font.render('-π', True, BLACK)
            screen.blit(text, (99+dis, 525))
          else:
            text=font.render(str(int(b))+'π', True, BLACK)
            screen.blit(text, (93+dis, 525))
      elif b%1!=0.5 and b>0:
          if b==1:
            text=font.render('π', True, BLACK)
            screen.blit(text, (105+dis, 525))
          else:
            text=font.render(str(int(b))+'π', True, BLACK)
            screen.blit(text, (100+dis, 525))
      elif b%1==0.5 and b>0:
          if b==0.5:
            text=font.render("π/2", True, BLACK)
            screen.blit(text, (97+dis, 525))
          else:
            text=font.render(str(int(b*2))+"π/2", True, BLACK)
            screen.blit(text, (92+dis, 525))
      elif b%1==0.5 and b<0:
          if b==-0.5:
            text=font.render("-π/2", True, BLACK)
            screen.blit(text, (93+dis, 525))
          else:
            text=font.render(str(int(b*2))+"π/2", True, BLACK)
            screen.blit(text, (89+dis, 525))
      dis+=48
      b+=0.5
  text=font.render('0', True, BLACK)
  screen.blit(text, (395, 525))
  font=pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 25)
  text=font.render('x', True, BLACK)
  screen.blit(text, (395, 555))
  n=-3
  dis=0
  while n<=-1:
      font=pygame.font.Font("C:\Windows\Fonts\Arial.ttf", 15)
      t=font.render(str(n), True, BLACK)
      screen.blit(t, (113+dis, 327))
      dis+=80
      n+=1

  def graphofcos():
      x=-3*math.pi
      dx=math.pi/1000
      x0=112
      dx0=1/10.4
      p=[]
      while x0<=688:
          pair=(x0, 300-192*math.cos(x))
          p.append(pair)
          x0+=dx0
          x+=dx
      pygame.draw.aalines(screen, BLUE, False, p)
  def graphofsin():
    x=-3*math.pi
    dx=math.pi/1000
    x0=112
    dx0=1/10.4
    p=[]
    while x0<=688:
        pair=(x0, 300-192*math.sin(x))
        p.append(pair)
        x0+=dx0
        x+=dx
    pygame.draw.aalines(screen, RED, False, p)
  graphofcos()
  graphofsin()
  pygame.display.flip()
pygame.quit()