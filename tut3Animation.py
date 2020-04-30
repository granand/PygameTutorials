import pygame
import os
pygame.init()

screen_width = 500
screen_height = 480

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("First Game")

# This goes outside the while loop, near the top of the program

walkRight = [pygame.image.load(os.path.join('images', 'R1.png')), pygame.image.load(os.path.join('images', 'R2.png')),
             pygame.image.load(os.path.join('images', 'R3.png')), pygame.image.load(os.path.join('images', 'R4.png')),
             pygame.image.load(os.path.join('images', 'R5.png')), pygame.image.load(os.path.join('images', 'R6.png')),
             pygame.image.load(os.path.join('images', 'R7.png')), pygame.image.load(os.path.join('images', 'R8.png')),
             pygame.image.load(os.path.join('images', 'R9.png'))]
walkLeft = [pygame.image.load(os.path.join('images', 'L1.png')), pygame.image.load(os.path.join('images', 'L2.png')),
            pygame.image.load(os.path.join('images', 'L3.png')), pygame.image.load(os.path.join('images', 'L4.png')),
            pygame.image.load(os.path.join('images', 'L5.png')), pygame.image.load(os.path.join('images', 'L6.png')),
            pygame.image.load(os.path.join('images', 'L7.png')), pygame.image.load(os.path.join('images', 'L8.png')),
            pygame.image.load(os.path.join('images', 'L9.png'))]
bg = pygame.image.load(os.path.join('images', 'bg.jpg'))
char = pygame.image.load(os.path.join('images', 'standing.png'))

clock = pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64
vel = 5

isJump = False
jumpCount = 10

left = False
right = False
walkCount = 0


def redraw_game_window():
    global walkCount
    win.blit(bg,(0,0))
    #   draw will always draw on a surface, here win is the surface
    if walkCount + 1 > 27:
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))


    #   Whenever you draw something on the surface, you should always update the display so that it will refresh
    pygame.display.update()

# main Loop
run = True
while run:
#    pygame.time.delay(5)
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < (screen_width - width - vel ):
        x += vel
        right = True
        left = False
    else:
        left = False
        right = False
        walkCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = True
            walkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10

    redraw_game_window()



pygame.quit()


