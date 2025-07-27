import pygame, random, os
from math import sin, cos, pi
pygame.init()

window_x = 1920
window_y = 1080

vertical_accelerate = 1/6
start = True
run = False
FireWorkList = []
fire = []
NumberOfFire = [0]
count = 0
color = []
index = -1

pygame.display.set_caption("Firework")
game_window = pygame.display.set_mode((window_x, window_y))

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)

fps_controller = pygame.time.Clock()

class FireWork:
    def __init__(self, vel, angle, size, color):
        self.angle = (angle * pi)/180
        self.vel_x = vel * cos(self.angle)
        self.vel_y = vel * sin(self.angle)
        self.x = window_x / 2
        self.y = window_y
        self.size = size
        self.reach = False
        self.color = color
        self.pop = False

    def drawFirework(self):
        pygame.draw.rect(game_window, self.color, pygame.Rect(self.x, self.y, self.size, self.size))

class Fire:
    def __init__(self, x, y, vel, angle, size, color):
        self.x = x
        self.y = y
        self.angle = angle
        self.vel_x = vel * cos(self.angle)
        self.vel_y = vel * sin(self.angle)
        self.size = size
        self.reach = False
        self.color = color

    def drawFire(self):
        pygame.draw.rect(game_window, self.color, pygame.Rect(self.x, self.y, self.size, self.size))
        

while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
        if event.type == pygame.MOUSEBUTTONUP and not run:
            run = True
            index += 1
            color.append(pygame.Color(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
            FireWorkList.append(FireWork(random.randrange(10, 20), random.randrange(180+75, 360-75), random.randrange(5, 10), color[index]))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        
    game_window.fill(black)

    for i in range(len(FireWorkList)):
        if not FireWorkList[i].reach:
            FireWorkList[i].drawFirework()
            FireWorkList[i].x += FireWorkList[i].vel_x
            FireWorkList[i].y += FireWorkList[i].vel_y
            FireWorkList[i].vel_y += vertical_accelerate
        if FireWorkList[i].vel_y >= 0  and not FireWorkList[i].reach:
            FireWorkList[i].pop = True
            FireWorkList[i].reach = True
            for j in range (random.randrange(5, 10)):
                count += 2
                fire.append(Fire(FireWorkList[i].x, FireWorkList[i].y, random.randrange(2, 3), random.randrange(200, 270), 3, color[i]))
                fire.append(Fire(FireWorkList[i].x, FireWorkList[i].y, random.randrange(2, 3), random.randrange(270, 330), 3, color[i]))
            NumberOfFire.append(count)
        if FireWorkList[i].pop:
            index += 1
            color.append(pygame.Color(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)))
            FireWorkList.append(FireWork(random.randrange(10, 20), random.randrange(180+75, 360-75), random.randrange(5, 10), color[index]))
            FireWorkList[i].pop = False
        if FireWorkList[i].reach:
            FireWorkList[i].x = -10
            FireWorkList[i].y = -10
            for FireNumber in range(NumberOfFire[i], NumberOfFire[i+1]):
                if not fire[FireNumber].reach:
                    fire[FireNumber].drawFire()
                    fire[FireNumber].x += fire[FireNumber].vel_x
                    fire[FireNumber].y += fire[FireNumber].vel_y
                    fire[FireNumber].vel_y += vertical_accelerate/3
                    if fire[FireNumber].y >= window_y:
                        fire[FireNumber].reach = True

    pygame.display.update()
    fps_controller.tick(60)

