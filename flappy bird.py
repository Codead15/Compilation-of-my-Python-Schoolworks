import pygame
import random

# initialize pygame
pygame.init()

# set window dimensions
screen_width = 288
screen_height = 512
screen = pygame.display.set_mode((screen_width, screen_height))

# set game variables
bird_pos = [50, 200]
bird_size = 34
gravity = 1
bird_jump = 14
pipe_width = 52
pipe_gap = 100
pipe_speed = 4
pipe_pos = [screen_width, 0]
score = 0
font = pygame.font.Font('freesansbold.ttf', 20)

# load images
background_img = pygame.image.load('background.png')
bird_img = pygame.image.load('bird.png')
pipe_img = pygame.image.load('pipe.png')
base_img = pygame.image.load('base.png')

# function to display score
def show_score():
    score_text = font.render('Score: ' + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# function to check collision
def check_collision():
    if bird_pos[1] + bird_size > base_pos:
        return True
    if bird_pos[1] < 0:
        return True
    if bird_pos[0] + bird_size > pipe_pos[0] and bird_pos[0] < pipe_pos[0] + pipe_width:
        if bird_pos[1] < pipe_pos[1] + pipe_height or bird_pos[1] + bird_size > pipe_pos[1] + pipe_height + pipe_gap:
            return True
    return False

# game loop
running = True
while running:
    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_pos[1] -= bird_jump

    # move pipes
    pipe_pos[0] -= pipe_speed
    if pipe_pos[0] < -pipe_width:
        pipe_pos[0] = screen_width
        pipe_pos[1] = random.randint(-200, 0)
        score += 1

    # move bird
    bird_pos[1] += gravity

    # check collision
    if check_collision():
        running = False

    # draw images
    screen.blit(background_img, (0, 0))
    screen.blit(bird_img, (bird_pos[0], bird_pos[1]))
    screen.blit(pipe_img, (pipe_pos[0], pipe_pos[1] + pipe_height + pipe_gap))
    screen.blit(pipe_img, (pipe_pos[0], pipe_pos[1] - pipe_height))
    screen.blit(base_img, (0, base_pos))

    # display score
    show_score()

    # update screen
    pygame.display.update()

# quit pygame
pygame.quit()
