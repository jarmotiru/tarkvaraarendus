import pygame

pygame.init()

#Defineerib värvid
HALL = (128, 128, 128)
ROHELINE = (0,255,0)
PUNANE = (255, 0, 0)
KOLLANE = (255, 255, 0)

#Määrab akna suuruse
screen=pygame.display.set_mode([300,300])
#Lisab programmiaknale nime
pygame.display.set_caption("Foor - Jarmo Tiru")


# Loop, mis hoiab akent avatuna
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Joonistab valgusfoori
    pygame.draw.rect(screen, HALL, [100, 10, 100, 270], 2)

    # Joonistab valgusfoori tuled
    pygame.draw.ellipse(screen, PUNANE, [110, 20, 79, 79])
    pygame.draw.ellipse(screen, KOLLANE, [110, 105, 79, 79])
    pygame.draw.ellipse(screen, ROHELINE, [110, 190, 79, 79])
    # Värskenda ekraan
    pygame.display.flip()

# Lõpeta Pygame'i
pygame.quit()


