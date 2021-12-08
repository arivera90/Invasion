import os
import pygame

class Game:

  hero_image_filename = ["invaders", "assets", "images", "hero.png"]

  def __init__(self):
    pass

  def run(self):
    pygame.init()

    window = pygame.display.set_mode([500,500], 0, 32)
    pygame.display.set_caption("Invaders!!!")
    pygame.mouse.set_visible(False)

    self.__hero_image = pygame.image.load(os.path.join(*Game.hero_image_filename)).convert_alpha()

    running = True

    while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False
    
      

      x,y = pygame.mouse.get_pos()
      x -= self.__hero_image.get_width() / 2
      y -= self.__hero_image.get_height() / 2

      window.fill((30,30,60))
      window.blit(self.__hero_image, (x,y))

      pygame.display.update()

    pygame.quit()