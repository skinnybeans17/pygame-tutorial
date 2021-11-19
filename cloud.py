import pygame
from random import randint, choice
from gameobject import GameObject

class Cloud(GameObject):
  def __init__(self):
    super(Cloud, self).__init__(0, 0, 'cloud-1.png')
    self.dx = 0
    self.reset()

  def move(self):
    self.x += self.dx
    if self.x > 500:
      self.reset()

  def get_cloud_image(self):
    return f"cloud-{randint(1, 3)}.png"

  def reset(self):
    self.x = -64
    self.y = randint(0, 500 - 64)
    self.dx = (randint(0, 200) / 100)
    self.surf = self.surf = pygame.image.load(self.get_cloud_image())