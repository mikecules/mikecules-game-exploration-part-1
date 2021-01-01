import pygame
import sys
import sprites
import random


def get_spaceship(screen):
    return sprites.SpaceShip(screen, 'spaceship.png', 640, 500)


def get_laser(screen, position_x, position_y, speed=3):
    return sprites.Laser(screen, 'Laser.png', position_x, position_y, speed)


def get_meteors(screen, number_of_meteors, max_reuse_count=1):
    meteors = []
    screen_width = screen.get_width()

    for i in range(number_of_meteors):
        meteor_index = random.randrange(1, 4)
        meteor_file = 'Meteor{0}.png'.format(meteor_index)
        x_pos = random.randrange(0, screen_width)
        x_direction = 1 if random.randint(0, 1) == 0 else -1
        x_speed = x_direction * (0.25 + random.randrange(1, 5) * random.random())
        y_speed = 1 + random.randrange(1, 5) * random.random()

        meteor = sprites.Meteor(screen, meteor_file, x_pos, -0.1 * screen.get_height(), x_speed, y_speed)
        meteor.max_reuse_count = max_reuse_count
        meteors.append(meteor)

    return meteors


def show_game_over_screen():
    pass


def show_game_start_screen():
    pass


def start_game(window_width=1200, window_height=720):
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    clock = pygame.time.Clock()

    spaceship = get_spaceship(screen)
    spaceship_group = pygame.sprite.GroupSingle(spaceship)

    laser_group = pygame.sprite.Group()

    meteors = get_meteors(screen, 1)
    meteor_group = pygame.sprite.Group(meteors)

    meteor_count = 1

    meteor_event = pygame.USEREVENT
    timer_interval_ms = 300
    pygame.time.set_timer(meteor_event, timer_interval_ms)

    game_states = {
        'START': 1,
        'PLAYING': 2,
        'ENDED': 3
    }

    game_state = game_states['PLAYING']

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == meteor_event:
                meteor_group.add(get_meteors(screen, meteor_count))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos_x, pos_y = pygame.mouse.get_pos()
                laser_group.add(get_laser(screen, pos_x, pos_y, 15))

        screen.fill((42, 45, 51))

        # Playing Game State
        if game_state == game_states['PLAYING']:
            laser_group.draw(screen)
            spaceship_group.draw(screen)
            meteor_group.draw(screen)

            laser_group.update()
            spaceship.update()
            meteor_group.update()

            if pygame.sprite.spritecollide(spaceship_group.sprite, meteor_group, True):
                spaceship_group.sprite.collide(1)

            for laser in laser_group.sprites():
                if pygame.sprite.spritecollide(laser, meteor_group, True):
                    laser.kill()

        # Ended Game State
        elif game_state == game_states['ENDED']:
            show_game_over_screen()

        # Beginning of Game State
        else:
            show_game_start_screen()

        if spaceship.health < 0:
            game_state = game_states['ENDED']

        pygame.display.update()
        clock.tick(120)


start_game()
