import pygame, sys, random

pygame.init()

#Ekraani seaded
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Animeerimine")

clock = pygame.time.Clock()

#Taustapildi laadimine
background = pygame.image.load("bg_rally.jpg").convert()

#Piltide lisamine
sinine_auto = pygame.image.load("f1_blue.png")
punane_auto = pygame.image.load("f1_red.png")
#Pöörab pildid teistpidi
sinine_auto_suund = pygame.transform.rotate(sinine_auto, 180)
punane_auto_suund = pygame.transform.rotate(punane_auto, 180)

#Kiirus ja asukoht
posX, posY = 0, 0
speedX, speedY = 3, 3

#Koordinaatide loomine ja lisamine massiivi
coords = []
for i in range(1):  #Määrab siniste autode arvu
    posX = random.randint(180, screenX - 270)
    posY = random.randint(-100, -50)
    coords.append([posX, posY])

#Skoori algväärtus
skoor = 0

#Mänguloogika tsükkel
gameover = False
while not gameover:
    # FPS
    clock.tick(120)                     #Määrab maksimaalse kaadrite kiiruse sekundis
    for i in pygame.event.get():        #Kontrollib akna sulgemist
       if i.type == pygame.QUIT:
           sys.exit()

    #Liigutab siniseid autosid alla ja uuendab nende asukohta
    for i in range(len(coords)):
        coords[i][1] += 1
        if coords[i][1] > screenY:
            coords[i][1] = random.randint(-100, -50)
            if i == 0:
                coords[i][0] = random.randint(180, 250)
            elif i == 1:
                coords[i][0] = random.randint(350, 450)
            skoor += 1

    #Taustapildi lisamine
    screen.blit(background, (0, 0))

    #Punase auto lisamine
    screen.blit(punane_auto_suund, (300, 350))

    #Loendist koordinaadid
    for i in range(len(coords)):
        screen.blit(sinine_auto_suund, (coords[i][0], coords[i][1]))

    #Skoori kuvamine
    font = pygame.font.Font(None, 36)
    skoor_text = font.render("Score: " + str(skoor), True, (255, 255, 255))
    screen.blit(skoor_text, (10, 10))

    #Värskendab ekraani
    pygame.display.flip()

pygame.quit()

