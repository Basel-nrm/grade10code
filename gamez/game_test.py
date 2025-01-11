'''
import pygame
pygame.init()


window = pygame.display.set_mode((640, 480))

window.fill((0, 0, 0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            

import pygame
pygame.init()
robot = pygame.image.load("robot.png")

x = 0
y = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    x+= 1
    clock.tick(120)
'''
'''
import pygame
pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    x += velocity
    if velocity > 0 and x+robot.get_width() >= 640:
        velocity = -velocity
    if velocity < 0 and x <= 0:
        velocity = -velocity

    clock.tick(120)
'''
'''
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot1 = pygame.image.load("robot.png")
x1 = 0
y1 = 240-robot1.get_height()
to_right1 = False
to_left1 = False
to_up1 = False
to_down1 = False

robot2 = pygame.image.load("robot.png")
x2 = 0
y2 = 0
target_x = 0
target_y = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            target_x = x1-robot1.get_width()/2
            target_y = y1-robot1.get_height()/2
            #player1
            if event.key == pygame.K_LEFT:
                to_left1 = True
            if event.key == pygame.K_RIGHT:
                to_right1 = True
            if event.key == pygame.K_UP:
                to_up1 = True
            if event.key == pygame.K_DOWN:
                to_down1 = True
            
            if event.type == pygame.KEYUP:
                #player1
                if event.key == pygame.K_LEFT:
                    to_left1 = False
                if event.key == pygame.K_RIGHT:
                    to_right1 = False
                if event.key == pygame.K_UP:
                    to_up1 = False
                if event.key == pygame.K_DOWN:
                    to_down1 = False
            
            if event.type == pygame.QUIT:
                exit()

        if x1+robot1.get_width() <= robot1.get_width():
            x1 = 0
        if x1+robot1.get_width() >= 640:
            x1 = 640 - robot1.get_width()
        if y1+robot1.get_height() <= robot1.get_height():
            y1 = 0
        if y1+robot1.get_height() >= 480:
            y1 = 480 - robot1.get_height()
        if to_right1:
            x1 += 2
        if to_left1:
            x1 -= 2
        if to_down1:
            y1 += 2
        if to_up1:
            y1 -= 2
        if x2 > target_x:
            x2 -= 2
        if x2 < target_x:
            x2 += 2
        if y2 > target_y:
            y2 -= 2
        if y2 < target_y:
            y2 += 2

    window.fill((0, 0, 0))
    window.blit(robot1, (x1, y1))
    window.blit(robot2, (x2, y2))
    pygame.display.flip()
    clock.tick(60)
'''
'''
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
x = 0
y = 240-robot.get_height()
clock = pygame.time.Clock()

to_right = False
to_left = False
to_up = False
to_down = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False
            
        if event.type == pygame.QUIT:
            exit()
    
    if x+robot.get_width() <= robot.get_width():
        x = 0 
    if x+robot.get_width() >= 640:
        x = 640 - robot.get_width()
    if y+robot.get_height() <= robot.get_height():
        y = 0 
    if y+robot.get_height() >= 480:
        y = 480 - robot.get_height()

    if to_right:
        x += 2
    if to_left:
        x -= 2
    if to_down:
        y += 2
    if to_up:
        y -= 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)
'''
'''
import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

window.fill((0, 0, 0))

robot = pygame.image.load("robot.png")

window.blit(robot, (0, 0))
window.blit(robot, (590, 0))
window.blit(robot, (0, 390))
window.blit(robot, (590, 390))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
'''
'''
import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

window.fill((0, 0, 0))

robot = pygame.image.load("robot.png")

window.blit(robot, (60, 200))
window.blit(robot, (110, 200))
window.blit(robot, (160, 200))
window.blit(robot, (210, 200))
window.blit(robot, (260, 200))
window.blit(robot, (310, 200))
window.blit(robot, (360, 200))
window.blit(robot, (410, 200))
window.blit(robot, (460, 200))
window.blit(robot, (510, 200))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
'''
'''
import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

window.fill((0, 0, 0))

robot = pygame.image.load("robot.png")
# row 1
window.blit(robot, (60, 0))
window.blit(robot, (110, 0))
window.blit(robot, (160, 0))
window.blit(robot, (210, 0))
window.blit(robot, (260, 0))
window.blit(robot, (310, 0))
window.blit(robot, (360, 0))
window.blit(robot, (410, 0))
window.blit(robot, (460, 0))
window.blit(robot, (510, 0))
# row 2
window.blit(robot, (60, 50))
window.blit(robot, (110, 50))
window.blit(robot, (160, 50))
window.blit(robot, (210, 50))
window.blit(robot, (260, 50))
window.blit(robot, (310, 50))
window.blit(robot, (360, 50))
window.blit(robot, (410, 50))
window.blit(robot, (460, 50))
window.blit(robot, (510, 50))
#row 3
window.blit(robot, (60, 100))
window.blit(robot, (110, 100))
window.blit(robot, (160, 100))
window.blit(robot, (210, 100))
window.blit(robot, (260, 100))
window.blit(robot, (310, 100))
window.blit(robot, (360, 100))
window.blit(robot, (410, 100))
window.blit(robot, (460, 100))
window.blit(robot, (510, 100))
# row 4
window.blit(robot, (60, 150))
window.blit(robot, (110, 150))
window.blit(robot, (160, 150))
window.blit(robot, (210, 150))
window.blit(robot, (260, 150))
window.blit(robot, (310, 150))
window.blit(robot, (360, 150))
window.blit(robot, (410, 150))
window.blit(robot, (460, 150))
window.blit(robot, (510, 150))
# row 5
window.blit(robot, (60, 200))
window.blit(robot, (110, 200))
window.blit(robot, (160, 200))
window.blit(robot, (210, 200))
window.blit(robot, (260, 200))
window.blit(robot, (310, 200))
window.blit(robot, (360, 200))
window.blit(robot, (410, 200))
window.blit(robot, (460, 200))
window.blit(robot, (510, 200))
#row 6
window.blit(robot, (60, 250))
window.blit(robot, (110, 250))
window.blit(robot, (160, 250))
window.blit(robot, (210, 250))
window.blit(robot, (260, 250))
window.blit(robot, (310, 250))
window.blit(robot, (360, 250))
window.blit(robot, (410, 250))
window.blit(robot, (460, 250))
window.blit(robot, (510, 250))
#row 7
window.blit(robot, (60, 300))
window.blit(robot, (110, 300))
window.blit(robot, (160, 300))
window.blit(robot, (210, 300))
window.blit(robot, (260, 300))
window.blit(robot, (310, 300))
window.blit(robot, (360, 300))
window.blit(robot, (410, 300))
window.blit(robot, (460, 300))
window.blit(robot, (510, 300))
#row 8
window.blit(robot, (60, 350))
window.blit(robot, (110, 350))
window.blit(robot, (160, 350))
window.blit(robot, (210, 350))
window.blit(robot, (260, 350))
window.blit(robot, (310, 350))
window.blit(robot, (360, 350))
window.blit(robot, (410, 350))
window.blit(robot, (460, 350))
window.blit(robot, (510, 350))
#row 9
window.blit(robot, (60, 400))
window.blit(robot, (110, 400))
window.blit(robot, (160, 400))
window.blit(robot, (210, 400))
window.blit(robot, (260, 400))
window.blit(robot, (310, 400))
window.blit(robot, (360, 400))
window.blit(robot, (410, 400))
window.blit(robot, (460, 400))
window.blit(robot, (510, 400))
#row 10
window.blit(robot, (60, 450))
window.blit(robot, (110, 450))
window.blit(robot, (160, 450))
window.blit(robot, (210, 450))
window.blit(robot, (260, 450))
window.blit(robot, (310, 450))
window.blit(robot, (360, 450))
window.blit(robot, (410, 450))
window.blit(robot, (460, 450))
window.blit(robot, (510, 450))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
'''
'''
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    x += 1
    clock.tick(60)
'''
'''
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    y += velocity
    if velocity > 0 and y+robot.get_width() >= 440:
        velocity = -velocity
    if velocity < 0 and y <= 0:
        velocity = -velocity

    clock.tick(60)
'''
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0
velocity = 1
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    x += velocity
    if x >= 590:
        x = 590
        y += 1

    clock.tick(60)
