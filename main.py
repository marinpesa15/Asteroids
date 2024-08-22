import pygame
from constants import *
from player import Player

pygame.init()

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Asteroids")
pygame.time.Clock()
dt = 0


def main():
  run = True
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()

  updatable.add(player)
  drawable.add(player)

  while run:
    dt = pygame.time.Clock().tick(60) / 1000
    win.fill("black")
    for entity in drawable:
      entity.draw(win)
    for entity in updatable:
      entity.update(dt)
    pygame.display.flip()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

  pygame.quit()


if __name__ == "__main__":
  main()