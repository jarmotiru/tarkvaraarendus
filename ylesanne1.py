import pygame

pygame.init()

#Defineerib värvid
MUST = (0, 0, 0)
VALGE = (255, 255, 255)
PUNANE = (255, 0, 0)


#Määrab akna suuruse
screen=pygame.display.set_mode([300,300])
#Lisab programmiaknale nime
pygame.display.set_caption("Lumemees - Jarmo Tiru")


done = False

clock = pygame.time.Clock()

#Põhiloop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    #Joonistab kolm erisuuruses valget ringi (lumememme keha)
    pygame.draw.ellipse(screen, VALGE, [120, 50, 60, 60])
    pygame.draw.ellipse(screen, VALGE, [110, 105, 80, 80])
    pygame.draw.ellipse(screen, VALGE, [100, 180, 100, 100])


    #Joonistab kaks musta ringi (silmad)
    pygame.draw.ellipse(screen, MUST, [135, 70, 10, 10])
    pygame.draw.ellipse(screen, MUST, [155, 70, 10, 10])

    #Joonistab hulknurga (lumememme nina)
    pygame.draw.polygon(screen, PUNANE, [[145, 85], [155, 85], [150, 100]])

    #Uuendab ekraani
    pygame.display.flip()
