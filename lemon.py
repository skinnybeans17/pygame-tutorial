import pygame
from random import randint, choice
from gameobject import GameObject
from constants import lanes

class Lemon(GameObject):
  def __init__(self):
    super(Lemon, self).__init__(0, 0, 'lemon.png')
    self.flavor = "sour"
    self.dx = (randint(0, 200) / 100) + 1
    self.dy = 0
    self.reset()

  def move(self):
    self.x += self.dx
    self.y += self.dy
    if self.x > 500:
      self.reset()

  def reset(self):
    self.x = -64
    self.y = choice(lanes)