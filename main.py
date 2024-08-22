import pygame
from constants import *

pygame.init()

win = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


def main():
  run = True

  while run:
    win.fill("black")
    pygame.display.flip()

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        run = False

  pygame.quit()


if __name__ == "__main__":
  main()