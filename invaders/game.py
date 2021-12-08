import os
import pygame
from pygame.locals import *
class Game:

  hero_image_filename = ["invaders", "assets", "images", "hero.png"]

  def __init__(self):
    pass

  def run(self):
    pygame.init()

    window = pygame.display.set_mode([500,500], 0, 32)
    pygame.display.set_caption("Invaders!!!")
    pygame.mouse.set_visible(False)
    pygame.joystick.init()
    joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    for joystick in joysticks:
        print(joystick.get_name())

    self.__hero_image = pygame.image.load(os.path.join(*Game.hero_image_filename)).convert_alpha()

    running = True
    motion = [0,0]
    x = 0
    y = 0
    while running:

      


      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False            
        if event.type == JOYAXISMOTION:
            print(event)
            if event.axis < 2:
                motion[event.axis] = event.value
                x += motion[0] * 5
                y += motion[1] * 5
        if event.type == JOYDEVICEADDED:
            joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
            for joystick in joysticks:
                print(joystick.get_name())
        if event.type == JOYDEVICEREMOVED:
            joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
     

      #x,y = pygame.mouse.get_pos()
      #x -= self.__hero_image.get_width() / 2
      #y -= self.__hero_image.get_height() / 2
      if x > 450:
        x=450
      if y > 450:
        y= 450
      if x < 0:
        x=0
      if y < 0:
        y= 0
    
      window.fill((30,30,60))
      window.blit(self.__hero_image, (x,y))

      pygame.display.update()

    pygame.quit()