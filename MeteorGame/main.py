import pygame
import sys
import sprites
import random


def get_spaceship(screen):
    return sprites.SpaceShip(screen, 'spaceship.png', 640, 500, 10)


def get_meteors(screen, number_of_meteors):
    meteors = []
    screen_width = screen.get_width()

    for i in range(number_of_meteors):
        meteor_index = random.randrange(1, 4)
        meteor_file = 'Meteor{0}.png'.format(meteor_index)
        x_pos = random.randrange(0, screen_width)
        x_direction = 1 if random.randint(0, 1) == 0 else -1
        x_speed = x_direction * (0.25 + random.randrange(1, 5) * random.random())
        y_speed = 1 + random.randrange(1, 5) * random.random()

        meteor = sprites.Meteor(screen, meteor_file, x_pos, 0, x_speed, y_speed)
        meteors.append(meteor)

    return meteors


def start_game(window_width=1200, window_height=720):
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()

    spaceship = get_spaceship(screen)
    spaceship_group = pygame.sprite.GroupSingle(spaceship)

    meteors = get_meteors(screen, 10)
    meteor_group = pygame.sprite.Group(meteors)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill((42, 45, 51))

        spaceship_group.draw(screen)
        spaceship.update()

        meteor_group.draw(screen)

        for meteor in meteors:
            meteor.update()

        pygame.display.update()
        clock.tick(120)


start_game()
