import pygame

class ScoreBoard(pygame.sprite.Sprite):
  def __init__(self, x, y, score):
    super(ScoreBoard, self).__init__()
    self.score = score
    self.display_score = score
    self.font = pygame.font.SysFont('arial', 30)
    self.surf = self.font.render(f"{self.score}", False, (255, 255, 255))
    self.dx = 0
    self.dy = 0
    self.x = x
    self.y = y

  def move(self):
    self.x += self.dx
    self.y += self.dy

  def update(self, points):
    self.score += points

  def render(self, screen):
    if self.score < self.display_score:
      self.display_score -= 1
    elif self.score > self.display_score:
      self.display_score += 1
    self.surf = self.font.render(f"{self.display_score}", False, (255, 255, 255))
    screen.blit(self.surf, (self.x, self.y))

  def reset(self):
    self.score = 0