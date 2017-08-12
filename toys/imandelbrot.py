from math import log

import pygame

width = 1200
height = 960

pygame.display.init()

screen = pygame.display.set_mode((width, height))
screen.fill(pygame.color.Color("black"))
xa = -2.1
xb = 0.8
ya = (xa - xb) * 0.5 * height / width
yb = - ya + 0.01
imax = 500

for y in range(height):
    pygame.display.flip()
    for x in range(width):
        c = complex(xa + (xb - xa) * x / width, ya + (yb - ya) * y / height)
        z = complex(0.0, 0.0)
        for i in range(imax):
            z = z * z + c
            if abs(z) >= 50:
                break
        if i < imax - 1:
            v = log(i + 1.5 - log(log(abs(z)), 2)) / 3.4
            if v < 1.0:
                red = v ** 4
                green = v ** 2.5
                blue = v  # blue
            else:
                v = max(0.0, 2.0 - v)
                red = v
                green = v ** 1.5
                blue = v ** 3  # sepia
            screen.set_at((x, y), (red * 255, green * 255, blue * 255))

while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.display.quit()
