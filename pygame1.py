import pygame
from pygame.locals import *

pygame.init()

surface = pygame.display.set_mode((640, 480))

ball = pygame.image.load("pydroball.png")
ballrect = ball.get_rect()
clock = pygame.time.Clock()

width = surface.get_width()
height = surface.get_height()

speed = [4, 4]
while True:
    for ev in pygame.event.get():
        if ev.type == QUIT:
            pygame.quit()
    clock.tick(60)
    surface.fill((0, 0, 0))
    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]
    surface.blit(ball, ballrect)
    pygame.display.flip()
Turtle.draw_fn("chin0", co=(30, 25, 31), mode=0)

Turtle.draw_fn("chin1", co=(204, 139, 124), mode=0)
Turtle.draw_fn("chin2", co=(204, 139, 124), mode=0)

Turtle.draw_fn("lip_lower", co=(214, 125, 100), mode=0)
Turtle.draw_fn("lip_upper", co=(186, 30, 21), mode=0)

Turtle.draw_fn("nostril", co=(8, 15, 29), mode=0)
Turtle.draw_fn("nose_curve", co=(128, 69, 56), mode=0)
Turtle.draw_fn("right_eyebrow", co=(12, 16, 22), mode=0)
Turtle.draw_fn("left_eyebrow", co=(12, 16, 22), mode=0)

Turtle.draw_fn("noseline", co=(12, 16, 22), mode=0)

Turtle.draw_fn("eyelid", co=(13, 15, 23), mode=0)
Turtle.draw_fn("eye", co=(17, 12, 20), mode=0)
Turtle.draw_fn("sclera", co=(230, 231, 229), mode=0)
Turtle.draw_fn("eyeball", co=(15, 25, 15), mode=0)
Turtle.draw_fn("eyeball_centre", co=(230, 231, 229), mode=0)

Turtle.draw_fn("hair_outline", co=(12, 16, 25), mode=0)
Turtle.draw_fn("hair_shade1", co=(12, 16, 25), mode=0)
Turtle.draw_fn("hair_shade2", co=(61, 44, 52), mode=0)
Turtle.draw_fn("hair_shade3", co=(119, 64, 75), mode=0)
Turtle.draw_fn("hair_shade4", co=(119, 64, 75), mode=0)
Turtle.draw_fn("hair_shade5", co=(61, 44, 52), mode=0)
Turtle.draw_fn("hair_shade6", co=(119, 64, 75), mode=0)
Turtle.draw_fn("hair_shade7", co=(61, 44, 52), mode=0)
Turtle.draw_fn("hair_shade8", co=(61, 44, 52), mode=0)

Turtle.draw_fn("throat", co=(245, 207, 171), mode=0)
Turtle.draw_fn("throat_shade1", co=(236, 180, 153), mode=0)
Turtle.draw_fn("throat_shade2", co=(236, 180, 153), mode=0)

Turtle.draw_fn("ear_line1", co=(16, 10, 😎, mode=0)
Turtle.draw_fn("ear_line2", co=(16, 10, 😎, mode=0)
Turtle.draw_fn("ear_line3", co=(16, 10, 😎, mode=0)
Turtle.draw_fn("ear_shade1", co=(212, 138, 124), mode=0)
Turtle.draw_fn("ear_shade2", co=(212, 138, 124), mode=0)
Turtle.draw_fn("ear_shade3", co=(212, 134, 122), mode=0)

Turtle.draw_fn("beard_shade1", co=(124, 77, 75), mode=0)
Turtle.draw_fn("beard_shade2", co=(127, 76, 76), mode=0)

Turtle.draw_fn("face_shade1", co=(209, 137, 122), mode=0)
Turtle.draw_fn("face_shade2", co=(208, 138, 119), mode=0)

Turtle.draw_fn("eye_shade1", co=(209, 143, 126), mode=0)
Turtle.draw_fn("eye_shade2", co=(209, 143, 126), mode=0)

Turtle.draw_fn("face_shade3", co=(245, 207, 171), mode=0)
Turtle.draw_fn("face_shade4", co=(240, 208, 169), mode=0)

Turtle.draw_fn("forhead_shade1", co=(202, 135, 119), mode=0)

Turtle.draw_fn("tshirt", co=(0, 30, 82), mode=0)
Turtle.draw_fn("tshirt_color1", co=(193, 36, 57), mode=0)
Turtle.draw_fn("tshirt_color2", co=(4, 31, 138), mode=0)
Turtle.draw_fn("tshirt_color3", co=(3, 35, 180), mode=0)

Turtle.draw_fn("end", retain=True, co=(230, 239, 234), mode=0)