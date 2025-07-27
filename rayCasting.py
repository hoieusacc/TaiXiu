import pygame
from math import sin, cos, tan, pi, sqrt, atan
pygame.init()

window_x = 1024
window_y = 512

velocity = 2
start = True
tile = 32
omega = 0.04
fov = pi / 3
half_fov = fov / 2
num_rays = 128
max_dist = 800
scale = 512 / (num_rays)

map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1],
       [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0 ,1],
       [1, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1 ,0 ,1 ,1 ,1],
       [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,1 ,0 ,1],
       [1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1 ,0 ,1 ,0 ,1],
       [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1 ,0 ,0 ,0 ,1],
       [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1 ,1 ,1 ,0 ,1],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0 ,0 ,1 ,0 ,1],
       [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1 ,1 ,1 ,0 ,1],
       [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,1 ,0 ,1],
       [1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 1 ,0 ,0 ,0 ,1],
       [1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1 ,0 ,1 ,1 ,1],
       [1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,1],
       [1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 1, 1 ,0 ,0 ,0 ,1],
       [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1 ,0 ,0 ,0 ,1],
       [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1 ,1 ,1 ,1]]

pygame.display.set_caption("Ray casting")
game_window = pygame.display.set_mode((window_x, window_y))

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255,255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
darkslategray = pygame.Color(47, 79, 79)
brown = pygame.Color(109, 98, 0)
lightblue = pygame.Color(173, 216, 230)
co = pygame.Color(34, 67, 56)

fps_controller = pygame.time.Clock()

def drawRect(x, y, width, height, color):
    pygame.draw.rect(game_window, color, pygame.Rect((x, y, width, height)))

def drawLine(start, end, color):
    pygame.draw.line(game_window, color, start, end)

def castRay(player, angle):
    x, y = player.x, player.y
    dist = 0
    while dist < max_dist:
        x += cos(angle)
        y += sin(angle)
        dist += 1
        if map[int(y // tile)][int(x // tile)]:
            dist = sqrt((x - player.x) ** 2 + (y - player.y) ** 2)
            return x, y ,dist
    return x, y, max_dist

def render_walls(player):
    for ray in range (num_rays):
        ray_angle = player.angle - half_fov + (ray / num_rays) * fov
        hit_x, hit_y, dist = castRay(player, ray_angle)

        corrected_depth = dist * cos(ray_angle - player.angle)
        wall_height = (tile * window_y) / corrected_depth
        drawRect(512 + ray * scale, (window_y / 2) - wall_height / 2, scale, wall_height, co)

class Player:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle

    def drawPlayer(self):
        pygame.draw.circle(game_window, green, (self.x, self.y), 8)

player = Player(80, 80, pi / 2)

while start:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            start = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        pygame.event.post(pygame.event.Event(pygame.QUIT))
    if keys[pygame.K_w]:
        if not map[int((player.y + velocity * sin(player.angle))) // tile][int((player.x + velocity * cos(player.angle))) // tile]:
                player.x += velocity * cos(player.angle)
                player.y += velocity * sin(player.angle)
    if keys[pygame.K_s]:
        if not map[int((player.y - velocity * sin(player.angle))) // tile][int((player.x - velocity * cos(player.angle))) // tile]:
                player.x -= velocity * cos(player.angle)
                player.y -= velocity * sin(player.angle)
    if keys[pygame.K_d]:
        if player.angle > 2 * pi:
            player.angle = 0
        player.angle += omega
    if keys[pygame.K_a]:
        if player.angle < 0:
            player.angle = 2 * pi
        player.angle -= omega

    game_window.fill(black)
    drawRect(512, 512 / 2, 512, 512 / 2, brown)
    drawRect(512, 0, 512, 512 / 2, lightblue)
    for i in range (-30, 30):
        ray_end_x, ray_end_y, dist = castRay(player, player.angle + (i * 1) * pi / 180)
        drawLine((player.x, player.y), (ray_end_x, ray_end_y), red)

    render_walls(player)
    for i in range (16):
        for j in range (16):
            if map[j][i]:
                drawRect(i * tile, j * tile, tile, tile, white)

    for i in range (16):
        drawLine((0, i * tile), (tile * 16, i * tile), darkslategray)
        drawLine((i * tile, 0), (i * tile, tile * 16), darkslategray)
    
    player.drawPlayer()

    pygame.display.update()
    fps_controller.tick(60)
