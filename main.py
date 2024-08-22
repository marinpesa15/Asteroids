import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
  pygame.init()
  win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption("Asteroids")
  clock = pygame.time.Clock()

  run = True
  dt = 0

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()

  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = updatable
  asteroid_field = AsteroidField()

  Player.containers = (updatable, drawable)
  Shot.containers = (shots, updatable, drawable)

  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  while run:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

    for entity in updatable:
      entity.update(dt)

    for asteroid in asteroids:
      if asteroid.collide(player):
        print("Game over!")
        run = False

    for asteroid in asteroids:
      for shot in shots:
        if shot.collide(asteroid):
          shot.kill()
          asteroid.split()
          break

    win.fill("black")
    for entity in drawable:
      entity.draw(win)

    pygame.display.flip()

  pygame.quit()


if __name__ == "__main__":
  main()