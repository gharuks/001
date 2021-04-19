import pygame
import random

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (225,225,0)
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500

background = pygame.image.load("background.png")
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
clock = pygame.time.Clock()

font=pygame.font.SysFont("Times new roman",25)

class Point:
  def __init__(self, _x: int, _y: int):
    self.x = _x
    self.y = _y
  
class Food:
  def __init__(self, *args, **kwargs):
    self.location = Point(0, 0)
    self.radius = 10
    self.image = pygame.image.load("apple.png")
    self.set_random_position()
  
  @staticmethod
  def own_round(value, base = 10):
    return base * round(value / 10)

  def set_random_position(self):
    x = self.own_round(random.randint(120,480))
    y = self.own_round(random.randint(100, 380))
    self.location.x = x
    self.location.y = y
  
  def draw(self):
    screen.blit(self.image, (self.location.x, self.location.y))
    pygame.display.flip()
 

class Snake:
  def __init__(self, *args, **kwargs):
    self.radius = 10
    self.body = [Point(100, 120), Point(120, 140)]
    self.dx = 10
    self.dy = 0
    self.is_add = False
  
  def head(self):
    return self.body[0]
  
  def move(self):
    if self.is_add:
      self.add_tail()

    for i in range(len(self.body) - 1, 0, -1):
      self.body[i].x = self.body[i - 1].x
      self.body[i].y = self.body[i - 1].y

    self.head().x += self.dx
    self.head().y += self.dy

    if self.head().x > WINDOW_WIDTH:
      self.head().x = 0
    if self.head().x < 0:
      self.head().x = WINDOW_WIDTH
  def draw(self, color):
    for i, point in enumerate(self.body):
      pygame.draw.circle(screen, color, (point.x, point.y), self.radius)
    
  def eat(self, foodx, foody):
    x = self.head().x
    y = self.head().y
    if foodx<=x<=foodx+15 and foody<=y<=foody+15:
      return True
    return False
  def collision(self, x2, y2):
    x = self.head().x
    y = self.head().y
    if x2<=x<=x2+15 and y2<=y<=y2+15:
      return True
    return False
      
  def add_tail(self):
    self.body.append(Point(0, 0))
    self.is_add = False
  def game_over(self):
    running = True
    while running:
      for event in pygame.event.get():
        if event.type==pygame.QUIT:
          pygame.quit()
          quit()
        if event.type==pygame.KEYDOWN:
          if event.key==pygame.K_SPACE:
            running=False
          if event.type==pygame.K_ESCAPE:
            pygame.quit()
            quit()
      background = pygame.image.load("mainmenu.jpg")
      screen.fill(WHITE)
      screen.blit(background, (0,0))
    
      font=pygame.font.SysFont("Times New Roman", 20, bold=True)
      text=font.render("GAME OVER",True,RED)
      screen.blit(text, (40, 100))
      if len(snake1.body)>len(snake2.body):
        text=font.render("1-Player won with score:"+str(len(snake1.body)-3),True,RED)
      elif len(snake1.body)<len(snake2.body):
        text=font.render("1-Player won with score:"+str(len(snake2.body)-3),True,RED)
      else: text=font.render("Good game: Draw",True,RED)
      screen.blit(text, (20, 120))
      text=font.render("Press SPACE to replay or ESCAPE to quit",True,RED)
      screen.blit(text, (40, 460))
      pygame.display.update()


def game_intro():
  intro=True
  while intro:
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        pygame.quit()
        quit()
      if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_p:
          intro=False
        if event.type==pygame.K_q:
          pygame.quit()
          quit()
    background = pygame.image.load("mainmenu.jpg")
    screen.fill(BLACK)
    screen.blit(background, (-10,-50))
    font=pygame.font.SysFont("Times New Roman", 20, italic=True)
    text=font.render("Welcome to",True,RED)
    screen.blit(text, (10, 100))
    text=font.render("'Snake Eat the Apple'!",True, RED)
    screen.blit(text, (20, 120))
    text=font.render("Press P to play or Q to quit",True,RED)
    screen.blit(text, (40, 140))
    pygame.display.update()

snake1 = Snake()
snake2 = Snake()
food = Food()
block=10
game_intro()
game_over = False

while not game_over:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      game_over = True
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE:
        running = False
      if event.key == pygame.K_RIGHT and snake1.dx!=-block:
        snake1.dx, snake1.dy = block, 0
      if event.key == pygame.K_LEFT and snake1.dx!= block:
        snake1.dx, snake1.dy = -block, 0
      if event.key == pygame.K_UP and snake1.dy != block:
        snake1.dx, snake1.dy = 0, -block
      if event.key == pygame.K_DOWN and snake1.dy != -block:
        snake1.dx, snake1.dy = 0, block

      if event.key == pygame.K_d and snake2.dx!=-block:
        snake2.dx, snake2.dy = block, 0
      if event.key == pygame.K_a and snake2.dx!= block:
        snake2.dx, snake2.dy = -block, 0
      if event.key == pygame.K_w and snake2.dy != block:
        snake2.dx, snake2.dy = 0, -block
      if event.key == pygame.K_s and snake2.dy != -block:
        snake2.dx, snake2.dy = 0, block
      
  if snake1.eat(food.location.x, food.location.y):
    snake1.is_add = True
    food.set_random_position()

  if snake2.eat(food.location.x, food.location.y):
    snake2.is_add = True
    food.set_random_position()
  for i in range(3, len(snake1.body)):
    if snake1.collision(snake1.body[i].x, snake1.body[i].y):
      snake1.body[i].x = snake1.body[i-500].x 
      snake1.body[i].y = snake1.body[i-500].y 
      for i in range(3,len(snake2.body)):
        if snake2.collision(snake2.body[i].x, snake2.body[i].y):
          snake2.game_over()
  screen.fill(WHITE)
  screen.blit(background, (0,0))
  def score(score, color, x, y):
    text=font.render("Score:"+str(score),True,color)
    screen.blit(text,[x, y])
  score(len(snake1.body)-2, BLACK, 0, 0)
  score(len(snake2.body)-2, YELLOW, 15, 15)
  snake1.move()
  snake2.move()

  
  
  snake1.draw(BLACK)
  snake2.draw(YELLOW)
  food.draw()

  pygame.display.flip()

  clock.tick(10)





