import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    
  def draw(self, surface):
    pygame.draw.circle(surface, "white", self.position, self.radius, 2)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()

    if self.radius <= ASTEROID_MIN_RADIUS:
      return 
    else:
      angle = random.uniform(20, 50)
      first_velocity = self.velocity.rotate(angle)
      second_velocity = self.velocity.rotate(-angle)
      new_radius = self.radius - ASTEROID_MIN_RADIUS

      asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
      asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
      asteroid1.velocity = first_velocity*1.2
      asteroid2.velocity = second_velocity*1.2
    