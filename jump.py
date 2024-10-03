import pygame
pygame.init()

#w == window
w_widht = 500
w_height = 500
screen = pygame.display.set_mode((w_widht, w_height))
pygame.display.set_caption("Adding jump logic")

#creating object
x = 0
y = 0
widht = 50
height = 50
vel = 1 #vel == velocity

clock = pygame.time.Clock() #regulate framrate

#jump varibales
is_jump = False #jump set to false 
jump_height = 10 

done = True
while done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    #moving the object by changing velocity
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and y > 0:
        y -= vel
    if keys[pygame.K_DOWN] and y < w_height-height:
        y += vel
    if keys[pygame.K_LEFT] and x > 0:
        x -= vel
    if keys[pygame.K_RIGHT] and x < w_widht-widht:
        x += vel    
    #making the object jump by multiplying y with jump_height
    if keys[pygame.K_SPACE]:
        is_jump = True

    if is_jump:
        if jump_height >=-10:
            neg = 1
            if jump_height < 0:
                neg = -1
            y -= (jump_height ** 2) * neg * 0.5
            jump_height -= 1
        else:
            jump_height = 10
            is_jump = False 
    
    
    
    screen.fill("white")
    pygame.draw.rect(screen, "black", (x,y,widht,height))
    clock.tick(60)
    pygame.display.flip()