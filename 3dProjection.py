import numpy as np
import pygame
from math import sin, cos, tan, pi
pygame.init()

window_x = 500
window_y = 500

start = True
run = False
angle = 0
scale = 2

pygame.display.set_caption("3D Projection")
game_window = pygame.display.set_mode((window_x, window_y))

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255,255)

fps_controller = pygame.time.Clock()

_points = np.array([[-25 ,-25, -25],
          [-25, 25 , -25],
          [25 , 25 , -25],
          [25 , -25, -25],
          [-25, -25, 25],
          [-25, 25 , 25],
          [25 , 25 , 25],
          [25 , -25, 25],])

_points = scale * _points

#projection = np.array([[1, 0, 0],
#                       [0, 1, 0]])
def rotationX(angle):
    rotationX = np.array([[1, 0, 0],
                          [0, cos(angle), -sin(angle)],
                          [0, sin(angle), cos(angle)]])
    return rotationX

def rotationY(angle):
    rotationY = np.array([[cos(angle), 0, sin(angle)],
                          [0, 1, 0],
                          [-sin(angle), 0, cos(angle)]])
    return rotationY

def rotationZ(angle):
    rotationZ = np.array([[cos(angle), -sin(angle), 0],
                          [sin(angle), cos(angle), 0],
                          [0, 0, 1]])
    return rotationZ

class Point:
    def __init__(self, position):
        self.x = position[0]
        self.y = position[1]
        self.z = position[2]

    def drawPoint(self):
        pygame.draw.circle(game_window, white, convert((self.x, self.y)), 1 * scale/2.5)

def convert(coords):
    return (coords[0] + 250, coords[1] + 250)

def drawLine(startPoint, endPoint):
    pygame.draw.aaline(game_window, white, startPoint, endPoint)

points = []
for i in range (8):
    points.append(Point(_points[i]))

while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.event.post(pygame.event.Event(pygame.QUIT))

    game_window.fill(black)

    for i in range (8):
        rotated = rotationX(angle) @ _points[i]
        rotated = rotationY(angle) @ rotated
        rotated = rotationZ(angle) @ rotated

        distance = 20
        fov = 60 * pi / 180

        proj = 1/((rotated[2] +  distance) * tan(fov))
        
        p = np.array([[1, 0, 0],
                      [0, 1, 0]])

        project2d = p @ rotated
        points[i].x = project2d[0]
        points[i].y = project2d[1]
        points[i].drawPoint()

    for i in range (4):
        drawLine((convert([points[i].x, points[i].y])), (convert([points[(i + 1) % 4].x, points[(i + 1) % 4].y])))
        drawLine((convert([points[i + 4].x, points[i + 4].y])), (convert([points[(i + 5) % 4 + 4].x, points[(i + 5) % 4 + 4].y])))

    for i in range (4):
        drawLine((convert([points[i].x, points[i].y])), (convert([points[i + 4].x, points[i + 4].y])))
    angle += 0.01
    pygame.draw.circle(game_window, white, convert((0, 0)), 2.5)

    pygame.display.update()
    fps_controller.tick(60)
