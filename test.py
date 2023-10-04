# importing pygame module
import pygame
 
# importing sys module
import sys
 
# initialising pygame
pygame.init()
 
# creating display
display = pygame.display.set_mode((500, 500))
 
# Creating the image surface
image = pygame.image.load('STR.jpg')
 
# putting our image surface on display surface
display.blit(image,(100,100))
 
# making the script wait for 5000 seconds
pygame.time.wait(500)
 
# creating a running loop
while True:
    display.blit(image,(100,100))
      # creating a loop to check events that are occurring
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # updating the display
    pygame.display.flip()
