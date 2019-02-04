import pygame
import sys
from settings import *
#Game clock / FPS 
clock = pygame.time.Clock()


def once_clicked(): 
	active = False
	background_light_green = (144, 238, 144)
	while not active:				
		for event in pygame.event.get():			
			if event.type == pygame.QUIT:
				active = True
				quit()
				
			if event.type == pygame.MOUSEBUTTONDOWN:
				once_clicked2()
				break	
			
			print(event)
						
		screen.fill(background_light_green)
		directions_message1()
		directions_message3()
		directions_message2()
		opening_message2()					
		pygame.display.update() 
		clock.tick(60)

def once_clicked2(): 
	active = False
	background_pink = (253, 90, 188)
	stop = True
	pygame.mixer.music.stop()
	while not active:				
		for event in pygame.event.get():			
			if event.type == pygame.QUIT:
				active = True
				quit()
			print(event)
			
		##Play words##				
		if stop: 
			stop = False
			play_sounds(the)
		
		screen.fill(background_pink)
		pygame.draw.rect(screen, white,(50,75,300,150))
		pygame.draw.rect(screen, white,(50,300,300,150))
		pygame.draw.rect(screen, white,(450,75,300,150))
		pygame.draw.rect(screen, white,(450,300,300,150))					
			
		pygame.display.update() 
		clock.tick(60)
				
			
