import pygame
import os

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Airball")


pygame.display.update()


# Set up the paddles
paddle_width = 10
paddle_height = 100
paddle_speed = 5
left_paddle_x = 50
left_paddle_y = screen_height / 2 - paddle_height / 2
right_paddle_x = screen_width - 50 - paddle_width
right_paddle_y = screen_height / 2 - paddle_height / 2

# Set up the ball
ball_size = 30
ball_speed = 1
ball_x = screen_width / 2 - ball_size / 2
ball_y = screen_height / 2 - ball_size / 2
ball_dx = ball_speed
ball_dy = ball_speed

# Set up the score
left_score = 0
right_score = 0
font = pygame.font.Font(None, 36)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and left_paddle_y > 0:
        left_paddle_y -= paddle_speed
    if keys[pygame.K_s] and left_paddle_y < screen_height - paddle_height:
        left_paddle_y += paddle_speed
    if keys[pygame.K_UP] and right_paddle_y > 0:
        right_paddle_y -= paddle_speed
    if keys[pygame.K_DOWN] and right_paddle_y < screen_height - paddle_height:
        right_paddle_y += paddle_speed

    # Move the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Check for collisions with the walls
    if ball_y < 0 or ball_y > screen_height - ball_size:
        ball_dy *= -1
    if ball_x < 0:
        right_score += 1
        ball_x = screen_width / 2 - ball_size / 2
        ball_y = screen_height / 2 - ball_size / 2
        ball_dx = ball_speed
        ball_dy = ball_speed
    if ball_x > screen_width - ball_size:
        left_score += 1
        ball_x = screen_width / 2 - ball_size / 2
        ball_y = screen_height / 2 - ball_size / 2
        ball_dx = -ball_speed
        ball_dy = ball_speed

    # Check for collisions with the paddles
    if ball_x < left_paddle_x + paddle_width and \
            left_paddle_y < ball_y + ball_size < left_paddle_y + paddle_height:
        ball_dx *= -1
    if ball_x + ball_size > right_paddle_x and \
            right_paddle_y < ball_y + ball_size < right_paddle_y + paddle_height:
        ball_dx *= -1

    # Draw the screen
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), (left_paddle_x, left_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, (255, 255, 255), (right_paddle_x, right_paddle_y, paddle_width, paddle_height))
    pygame.draw.rect(screen, (255, 255, 255), (ball_x, ball_y, ball_size, ball_size))
    left_score_text = font.render(str(left_score), True, (255, 255, 255))
    right_score_text = font.render(str(right_score), True, (255, 255, 255))
    screen.blit(left_score_text, (screen_width / 4 - left_score_text.get_width() / 2, 10))
    screen.blit(right_score_text, (3 * screen_width / 4 - right_score_text.get_width() / 2, 10))
    pygame.display.flip()

# Clean up
pygame.quit()
