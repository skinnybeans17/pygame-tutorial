from typing import Sequence
from animatedobject import AnimatedObject

def get_explosion_frames():
  frames = []
  for n in range(1, 23):
    frames.append((f"explosion-{n}.png", 1))
    
  return frames

class Explosion(AnimatedObject):
  def __init__(self, x, y):
    sequence = get_explosion_frames()
    super().__init__(x, y, sequence)
    self.play_mode = 'once'