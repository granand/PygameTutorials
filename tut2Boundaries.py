import pygame
pygame.init()

screen_width = 500
screen_height = 500

win = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 40
height = 60
vel = 5

isJump =  False
jumpCount = 10


run = True
while run:
    pygame.time.delay(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < (screen_width - width - vel ):
        x += vel
    if not(isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < (screen_height - height - vel):
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
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

    win.fill((0, 0, 0))

#   draw will always draw on a surface, here win is the surface
#   Next parameter is the color which is RGB, and next is the co-ordinates, length and width for rectangle
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
#   Whenever you draw something on the surface, you should always update the display so that it will refresh
    pygame.display.update()


pygame.quit()


