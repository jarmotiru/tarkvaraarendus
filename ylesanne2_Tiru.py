import pygame

pygame.init()

#Mängu akna suurus
size = (640, 480)
screen = pygame.display.set_mode(size)

#Mängu nimi
pygame.display.set_caption("Ülesanne 2")

#Taustapilt
bg = pygame.image.load("bg_shop.png")
bg = pygame.transform.scale(bg, size)

#Poemüüja suurus
seller = pygame.image.load("seller.png")
seller = pygame.transform.scale(seller, (257, 307))

#Jutumulli suurus
chat = pygame.image.load("chat.png")
chat = pygame.transform.scale(chat, (255, 211))

#Jutumulli tekst
font = pygame.font.Font(pygame.font.match_font('arial'), 22)   #Teksti suurus, ja font
text = font.render("Tere, olen Jarmo Tiru", True, (255, 255, 255))   #Tekst ja teksti värv

#tekstikasti suurus
text_width = text.get_rect().width
text_height = text.get_rect().height

#Mängu tsükkel
done = False
while not done:
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           done = True

   #Tausta joonistamine
   screen.blit(bg, (0, 0))

   #Poemüüja asukoht
   screen.blit(seller, [105,158])

   #Jutumulli asukoht
   screen.blit(chat, [247,63])

   #Jutumulli teksti joonistamine, asukoht
   screen.blit(text, [375 - text_width / 2, 150 - text_height / 2])

   pygame.display.flip()

pygame.quit()