from typing import Sequence
from animatedobject import AnimatedObject

def get_explosion_frames():
  frames = []
  for n in range(1, 13):
    frames.append((f"pop-{n}.png", 1))
    
  return frames

class Pop(AnimatedObject):
  def __init__(self, x, y):
    sequence = get_explosion_frames()
    super().__init__(x, y, sequence)
    self.play_mode = 'once'