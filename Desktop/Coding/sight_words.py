
import pygame
import sys 
import time
from settings import *
from game_logic import *


#initates game
pygame.init()
settings()
opening_message()
gameIcon = pygame.image.load('puppy.png')
pygame.display.set_icon(gameIcon)

##Start button##
play_button = pygame.image.load('playbutton.png')
def start_button(x,y):
	screen.blit(play_button, (x,y))
x = (300)
y = (227) 
	
##Game main loop## 
def mainloop(): 
	active = False
	background_blue = (8, 156, 204)
	play_ambient()
	while not active:				
		for event in pygame.event.get():			
			if event.type == pygame.QUIT:
				active = True		
	
			if event.type == pygame.MOUSEBUTTONDOWN:
				background_blue = background_light_green
				screen.fill(background_light_green)
				once_clicked()
				break	
					
			print(event) 	
		screen.fill(background_blue)
		opening_message()
		start_button(x,y)	
		
		pygame.display.update() 
		clock.tick(60)
	
mainloop()	
pygame.quit()
quit()

