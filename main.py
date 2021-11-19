import pygame
from pygame import mixer
from random import randint, choice
from gameobject import GameObject
from apple import Apple
from strawberry import Strawberry
from bomb import Bomb
from player import Player
from cloud import Cloud
from animatedobject import AnimatedObject
from explosion import Explosion
from pop import Pop
from lemon import Lemon
from scoreboard import ScoreBoard
from pointssprite import PointsSprite

mixer.init()
mixer.music.load('theme.mp3')
mixer.music.play(99)

point_sound = pygame.mixer.Sound("point.wav")
bomb_sound = pygame.mixer.Sound("explode.wav")
splat_sound = pygame.mixer.Sound("splat.mp3")

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode([501, 501])

all_sprites = pygame.sprite.Group()
fruit_sprites = pygame.sprite.Group()
explosion_sprites = pygame.sprite.Group()
pop_sprites = pygame.sprite.Group()

all_sprites.add(Cloud())
all_sprites.add(Cloud())
all_sprites.add(Cloud())
score = ScoreBoard(30, 30, 0)
all_sprites.add(score)

apple = Apple()
strawberry = Strawberry()
lemon = Lemon()
fruit_sprites.add(apple)
fruit_sprites.add(strawberry)
fruit_sprites.add(lemon)

player = Player()
bomb = Bomb()

all_sprites.add(player)
all_sprites.add(apple)
all_sprites.add(strawberry)
all_sprites.add(lemon)
all_sprites.add(bomb)

clock = pygame.time.Clock()

def make_explosion(x, y):
  explosion = Explosion(x, y)
  explosion_sprites.add(explosion)

def make_pop(x, y):
  pop = Pop(x, y)
  pop_sprites.add(pop)

game_state = 'ready'
running = True
while running:
  if game_state == 'ready':
    game_state = 'playing'
  elif game_state == 'playing':
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
      elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
          running = False
        elif event.key == pygame.K_LEFT:
          player.left()
        elif event.key == pygame.K_RIGHT:
          player.right()
        elif event.key == pygame.K_UP:
          player.up()
        elif event.key == pygame.K_DOWN:
          player.down()
  elif game_state == 'game_over':
    game_state = "ready"

  screen.fill((170, 230, 255))

  for entity in all_sprites:
    entity.move()
    entity.render(screen)
    if entity != player: 
      pass
  fruit = pygame.sprite.spritecollideany(player, fruit_sprites)
  if fruit:
    if fruit.flavor == "sweet":
      pygame.mixer.Sound.play(point_sound)
      make_pop(fruit.x, fruit.y)
      points = PointsSprite(fruit.x, fruit.y, 2)
      score.update(2)
      all_sprites.add(points)
      fruit.reset()
    elif fruit.flavor == "sweeter":
      pygame.mixer.Sound.play(point_sound)
      make_pop(fruit.x, fruit.y)
      points = PointsSprite(fruit.x, fruit.y, 3)
      score.update(3)
      all_sprites.add(points)
      fruit.reset()
    elif fruit.flavor == "sour":
      make_pop(player.x, player.y)
      points = PointsSprite(fruit.x, fruit.y, -1)
      score.update(-1)
      all_sprites.add(points)
      player.stun()
      pygame.mixer.Sound.play(splat_sound)
      fruit.reset()

  fruit = pygame.sprite.spritecollideany(bomb, fruit_sprites)
  if fruit:
    make_explosion(fruit.x, fruit.y)
    pygame.mixer.Sound.play(bomb_sound)
    points = PointsSprite(fruit.x, fruit.y, -3)
    all_sprites.add(points)
    score.update(-3)
    fruit.reset()

  if pygame.sprite.collide_rect(player, bomb):
    pygame.mixer.Sound.play(bomb_sound)
    running = False

  for explosion in explosion_sprites:
    explosion.render(screen)
    if explosion.playing == False: 
      explosion.kill()

  pygame.display.flip()
  clock.tick(30)