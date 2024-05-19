# Imported Packages
import pygame
import random 
import time
import math
import os
pygame.font.init()

pygame.init()

#Pygame Window
WIDTH, HEIGHT = 650, 300
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sky Dodge")

# Background image
BG = pygame.image.load("Wallpapers/Sky.jpg")


# Defined Functions
PLAYER_WIDTH = 30
PLAYER_HEIGHT = 60

PLAYER_VEL = 5

STAR_WIDTH = 10
STAR_HEIGHT = 10
STAR_VEL = 3


# Font 
FONT = pygame.font.SysFont("comicsans MS", 30)


def draw(player, elapsed_time, stars):
    WIN.blit(BG , (0, 0))
    
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "Black")
    WIN.blit(time_text, (10, 10))
    
    pygame.draw.rect(WIN, "blue", player)
    
    for star in stars:
        pygame.draw.rect(WIN, "red", star)
    
    
    pygame.display.update()


# Adding Player and Projectiles
def main():
    run = True
    
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT )
    
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    
    star_add_increment = 2000
    star_count = 0
    
    stars = []
    hit = False
    
    
    
# Game Loop
    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            
            star_add_increment = max(200, star_add_increment - 20 )
                
            star_count = 0
            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
            
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT]and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL 
            
        # Moving projectiles and collision    
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break
            
        if hit:
            lost_text = FONT.render("Game Over!", 1, "Black")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
            
            
        draw(player, elapsed_time, stars)    
            
pygame.quit

if __name__ == "__main__":
    main()  
                