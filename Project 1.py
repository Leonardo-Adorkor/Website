import pygame
from pygame.locals import *

pygame.init()

screen_width = 300
screen_height = 200

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Platfomer')

#define game variables
tile_size = 20

#load images
sun_img = pygame.image.load("Wallpapers/Sun.jpg")
bg_img = pygame.image.load("Wallpapers/Sky.jpg")

def draw_grid():
    for line in range(0, 50):
        pygame.draw.line(screen, (255,255,255),(0, line * tile_size),(screen_width,line * tile_size))
        pygame.draw.line(screen, (255,255,255),(line * tile_size, 0), (line * tile_size , screen_height))


class world():
    def __init__(self, data):
        self.tile_list = []
        
        #load images
        dirt_img = pygame.image.load('Wallpapers/land.jpg')
        land_img = pygame.image.load('Wallpapers/land.jpg')
        
        row_count = 0
        for row in data:
            col_count = 0
            for tile in row:
                if tile == 1 :
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2 :
                    img = pygame.transform.scale(land_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_count * tile_size
                    img_rect.y = row_count * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                col_count += 1
            row_count += 1
            
    def draw(self):
        for tile in self.tile_list:
            screen.blit(tile[0], tile[1])
            
world_data = [
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 0, 7, 0, 0, 0, 8, 1],
[1, 0, 7, 0, 0, 7, 0, 0, 0, 2, 2],
[1, 7, 0, 0, 2, 2, 2, 0, 0, 0, 1],
[1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0],
[1, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1],
]

world = world(world_data)

run = True
while run == True:
    
    screen.blit(sun_img,(20,20))
    screen.blit(bg_img, (10,10))
    
    world.draw()
        
    draw_grid()
    
    print(world.tile_list)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            
    pygame.display.update()
            
pygame.quit()