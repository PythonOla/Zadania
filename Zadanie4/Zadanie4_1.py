import pygame, sys, math;

def getDecayValue(val, max_decay):
    decay_abs = min(abs(val), max_decay)
    if val > 0:
        return decay_abs 
    else:
        return -decay_abs

SPEED_DECAY = 1
ACCEL_DECAY = 10000000
ACCEL_SENSITIVITY = 20

def main():
   clock = pygame.time.Clock()

   pygame.display.set_caption('Let\'s play ball')
#    icon = pygame.image.load('ikonka.jpg')
#    pygame.display.set_icon(icon)

#    pygame.mixer.music.load(r'C:\Users\witol\Documents\UJ\PYTHON\GAME\music.mp3')
#    pygame.mixer.music.play(-1)

   size = width, height = 800, 600
   screen = pygame.display.set_mode(size)

   speed = [0, 0]
   accel = [0, 0]

   image=pygame.image.load(r'C:\Users\hp\source\repos\pythonola\zadania\zadanie4\wallpaper.jpg')
   image = pygame.transform.scale(image, size)

   surf_center = (
       (width-image.get_width())/2,
       (height-image.get_height())/2
   )

   screen.blit(image, surf_center)
   ball = pygame.image.load(r'C:\Users\hp\source\repos\pythonola\zadania\zadanie4\yarn.png')
   ball = pygame.transform.scale(ball, (75, 75))

   screen.blit(ball, (width/2, height/2))

   ballrect = ball.get_rect(center=(width/2, height/2))
   pygame.display.flip()


   while True:
        clock.tick(60)
        pygame.time.delay(50)

        for event in pygame.event.get():
           if event.type == pygame.QUIT: sys.exit()

           keys = pygame.key.get_pressed()
           if keys[pygame.K_ESCAPE]: sys.exit()

           if keys[pygame.K_UP]:
               accel[1] -= ACCEL_SENSITIVITY 
           elif keys[pygame.K_DOWN]:
               accel[1] += ACCEL_SENSITIVITY
           elif keys[pygame.K_LEFT]:
               accel[0] -= ACCEL_SENSITIVITY
           elif keys[pygame.K_RIGHT]:
               accel[0] += ACCEL_SENSITIVITY

        ballrect = ballrect.move(speed)
        if ballrect.left < 0 or ballrect.right > width:
           speed[0] = -speed[0]
           accel[0] = -accel[0]
        if ballrect.top < 0 or ballrect.bottom > height:
           speed[1] = -speed[1]
           accel[1] = -accel[1]

        speed[0] += accel[0]
        speed[1] += accel[1]
        accel[0] -= getDecayValue(accel[0], ACCEL_DECAY)
        accel[1] -= getDecayValue(accel[1], ACCEL_DECAY)
        speed[0] -= getDecayValue(speed[0], SPEED_DECAY)
        speed[1] -= getDecayValue(speed[1], SPEED_DECAY)
        print(speed, accel)
    

        screen.blit(image,surf_center)
        screen.blit(ball,ballrect)
        pygame.display.flip()

if __name__ == '__main__':
    main()
    pygame.quit()
    sys.exit()