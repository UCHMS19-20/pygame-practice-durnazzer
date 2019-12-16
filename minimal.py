import sys
import pygame
import time

# Initialize pygame so it runs in the background and manages things
pygame.init()

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (400, 300) )

# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()


    screen.fill((255, 0, 0))
    pygame.display.flip()

    time.sleep(1)

    screen.fill((60, 230, 30))
    pygame.display.flip()

    time.sleep(1)
