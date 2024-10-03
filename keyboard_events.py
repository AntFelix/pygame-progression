import pygame
pygame.init()

#w == window
w_widht = 300
w_height = 300
screen = pygame.display.set_mode((w_widht, w_height))
screen.fill("white")
pygame.display.set_caption("Handling keyboard events")

#creating object
x = 0
y = 0
widht = 50
height = 50
vel = 1 #vel == velocity

clock = pygame.time.Clock() #regulate framrate
done = True
while done: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = False
    #moving the object by changing velocity
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_DOWN]:
        y += vel
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_RIGHT]:
        x += vel    
    
    screen.fill("white")
    pygame.draw.rect(screen, "black", (x,y,widht,height))
    clock.tick(60)
    pygame.display.flip()