import pygame
import sys
import random
import GameObjects.Background as Background
import GameObjects.Interactive as Interactive


def init_screen(width, height):
    return pygame.display.set_mode((width, height))


def get_bg_objects(screen):
    return {
        'woodBackground': Background.Wood(pygame, screen, 'Wood_BG.png'),
        'landBackground': Background.Land(pygame, screen, 'Land_BG.png'),
        'waterBackground': Background.Water(pygame, screen, 'Water_BG.png')
    }


def get_cross_hair(screen):
    return Interactive.CrossHair(pygame, screen, 'crosshair.png')


def get_duck(screen, min_x, max_y):
    duck = Interactive.Duck(pygame, screen, 'duck.png')
    duck_width = duck.get_width()
    duck_height = duck.get_height()

    start_x = random.randrange(duck_width + min_x, screen.get_width() - duck_width)
    start_y = random.randrange(duck_height, screen.get_height() - max_y - duck_height)

    duck.set_position(start_x, start_y)

    return duck


def get_ducks(number_of_ducks, screen, min_x, max_y):
    ducks = []

    for duck in range(number_of_ducks):
        ducks.append(get_duck(screen, min_x, max_y))

    return ducks


def fetch_clouds(screen, number_of_clouds):
    cloud_image_assets = {
        'cloud1': 'Cloud1.png',
        'cloud2': 'Cloud2.png'
    }

    if number_of_clouds < 1:
        return None

    clouds = {}

    for i in range(number_of_clouds):
        cloud_key = random.randrange(1, len(cloud_image_assets) + 1)
        image_asset = cloud_image_assets['cloud{0}'.format(cloud_key)]

        cloud = Background.Cloud(pygame, screen, image_asset)
        position = (
            random.randrange(
                # Allow for the cloud to be off screen to the left of up to 75%
                random.randrange(
                    int(-0.75 * cloud.get_width()),
                    0
                ),
                screen.get_width()
            ),
            random.randrange(
                random.randrange(
                    int(-0.75 * cloud.get_height()),
                    0
                ),
                screen.get_height() * 0.5)
        )

        cloud.set_position(*position)
        clouds[i] = cloud

    return clouds


def get_font(font_size=60):
    return pygame.font.Font(None, font_size)


def get_text(font, text, colour=(255, 255, 255)):
    return font.render(text, True, colour)


def start_game(width=1280, height=720, framerate=120, **kwargs):
    pygame.init()
    pygame.mouse.set_visible(False)
    screen = init_screen(width, height)
    clock = pygame.time.Clock()

    # Images
    bg_objects = get_bg_objects(screen)
    max_cloud_count = kwargs.get('cloud_count') or 20
    max_duck_count = kwargs.get('duck_count') or 10

    clouds = fetch_clouds(screen, max_cloud_count)
    cross_hair = get_cross_hair(screen)
    ducks = get_ducks(max_duck_count, screen, 0, bg_objects['landBackground'].get_height())
    font = get_font()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # detect collision by checking the duck that is last drawn first!
                for (i, duck) in reversed(list(enumerate(ducks))):
                    duck_rect = duck.get_rect(topleft=duck.get_position())

                    if duck_rect.collidepoint(event.pos):
                        print('Duck #{0} hit!'.format(i))

                        # This does collide method does nothing right now but could
                        # be used to perform an animation before deleting it :)
                        duck.collide()

                        # remove it the duck from the list
                        del ducks[i]

                        # Delete only the first duck hit
                        break

        # Non interactive background animations
        bg_objects['woodBackground'].animate()
        bg_objects['landBackground'].animate()
        bg_objects['waterBackground'].animate()

        # Ducks
        for duck in ducks:
            duck.animate()

        # Clouds
        for (cloud_id, cloud_object) in clouds.items():
            cloud_object.animate()

        if len(ducks) == 0:
            text_surface = get_text(font, 'Congratulations You Won!')
            screen.blit(
                text_surface,
                text_surface.get_rect(
                    center=(
                        (screen.get_width()) / 2,
                        ((screen.get_height()) / 2)
                    ))
            )

        cross_hair.animate()

        pygame.display.update()
        clock.tick(framerate)


start_game(duck_count=10, cloud_count=10)
