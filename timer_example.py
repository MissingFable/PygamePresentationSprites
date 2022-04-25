import pygame
import sys
import math

screen_size = [800, 800]

pygame.init()

display = pygame.display.set_mode((screen_size))
clock = pygame.time.Clock()

frame_count = 0

max_time = 30

current_time = max_time

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    current_time = (max_time - math.floor(frame_count/60))
    frame_count += 1

    # when restarting game, reset current_time and frame_count to 0

    print(current_time)

    pygame.display.update()
    clock.tick(60)