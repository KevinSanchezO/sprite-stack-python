import pygame, sys, os

DISPLAY_SIZE = (720,720)
SURFACE_SIZE = (200,200)

frame = 0
rotation_type = "right"
spread = 1

pygame.init()

pygame.display.set_caption("Sprite Stacking")
screen = pygame.display.set_mode(DISPLAY_SIZE)
display = pygame.Surface(SURFACE_SIZE)

images_stack = [pygame.image.load('stack/'+img) for img in os.listdir('stack')]

clock = pygame.time.Clock()

def render_sprite_stack(surface, images, pos, rotation, spread):
    for i, img in enumerate(images):
        rotated_image = pygame.transform.rotate(img, rotation)
        surface.blit(rotated_image, (pos[0] - rotated_image.get_width() // 2, pos[1] -rotated_image.get_height() // 2 - i * spread))

def modify_rotation_type(new_rotation):
    global rotation_type
    rotation_type = new_rotation

def modify_rotation():
    global frame
    if rotation_type == "right":
        frame += 1.5
    elif rotation_type == "left":
        frame -= 1.5

def modify_spread(spread_value):
    global spread

    if spread_value > 0:
        if spread + spread_value > 10:
            return
    else:
        if spread + spread_value < 1:
            return
    spread += spread_value

while True:
    display.fill((0,0,0))

    modify_rotation()

    render_sprite_stack(display, images_stack, (100, 130), frame, spread)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                modify_rotation_type("left")
            if event.key == pygame.K_RIGHT:
                modify_rotation_type("right")
            if event.key == pygame.K_UP:
                modify_spread(1)
            if event.key == pygame.K_DOWN:
                modify_spread(-1)
                
    screen.blit(pygame.transform.scale(display, screen.get_size()), (0, 0))
    pygame.display.update()
    clock.tick(60)