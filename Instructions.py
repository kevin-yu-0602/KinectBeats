import pygame
SHRINK_FACTOR = 2/3
freeplay_lh = pygame.image.load('resources/freeplay_lh.jpg')
freeplay_lh = pygame.transform.scale(freeplay_lh, (int(222*SHRINK_FACTOR), int(186*SHRINK_FACTOR)))

freeplay_rh = pygame.image.load('resources/freeplay_rh.jpg')
freeplay_rh = pygame.transform.scale(freeplay_rh, (int(176*SHRINK_FACTOR), int(197*SHRINK_FACTOR)))

loop_rh = pygame.image.load('resources/loop_rh.jpg')
loop_rh = pygame.transform.scale(loop_rh, (int(220*SHRINK_FACTOR), int(184*SHRINK_FACTOR)))

loop_lh = pygame.image.load('resources/loop_lh.jpg')
loop_lh = pygame.transform.scale(loop_lh, (int(218*SHRINK_FACTOR), int(182*SHRINK_FACTOR)))

loop_select = pygame.image.load('resources/loop_select.jpg')
loop_select = pygame.transform.scale(loop_select, (int(280*SHRINK_FACTOR), int(267*SHRINK_FACTOR)))

mode_change = pygame.image.load('resources/mode_change.jpg')
mode_change = pygame.transform.scale(mode_change, (int(254*SHRINK_FACTOR), int(268*SHRINK_FACTOR)))