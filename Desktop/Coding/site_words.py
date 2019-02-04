import pygame
import sys 
import time
from settings import settings

#initates game
pygame.init()
settings()

# ~ """DISPLAY & IMAGES"""
# ~ #defines the display size
# ~ display_width = 800
# ~ display_height = 600
# ~ background_blue = (8, 156, 204)
# ~ background_light_green = (144, 238, 144)
# ~ text_black = (0, 0, 0)
# ~ screen = pygame.display.set_mode((display_width, display_height))
# ~ #defines the window title caption
# ~ pygame.display.set_caption("Grace's Sight Words Game")

"""mouse event checks"""
mouse = pygame.mouse.get_pressed()


"""user defined images"""
play_button = pygame.image.load('playbutton.png')

def start_button(x,y):
	screen.blit(play_button, (x,y))

x = (300)
y = (227) 

def opening_message():
	basicfont = pygame.font.SysFont(None, 48)
	text = basicfont.render('Click to Start!', True, (255, 255, 0), (8, 156, 204))
	textrect = text.get_rect()
	screen.blit(text, (300, 350))
	


#Game clock / FPS 
clock = pygame.time.Clock()

#flag


#Once start is clicked
def game_once_clicked():
	active = False
	while not active:
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				active = True
	
	
	screen.fill(background_light_green)
	pygame.display.update() 
	clock.tick(60)

#game main loop
def main_loop():
	active = False
	while not active: 
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				active = True		
	
		print(event) 
				
		if event.type == pygame.MOUSEBUTTONDOWN:
			game_once_clicked()
			break
			
			
	screen.fill(background_blue)				
	opening_message()
	start_button(x,y)	
		
	pygame.display.update() 
	clock.tick(60)
	

	



pygame.quit()
quit()

